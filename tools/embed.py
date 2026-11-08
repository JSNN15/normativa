"""Vectoriza los fragmentos (passage, 512 dim) y guarda vectores int8 + índice compacto para el navegador."""
import json, os, time, subprocess, base64, math, sys
D = os.path.dirname(os.path.abspath(__file__))
KEY = os.environ.get('NVIDIA_API_KEY') or sys.exit('Falta la variable de entorno NVIDIA_API_KEY')
DIM = 512
data = json.load(open(f'{D}/chunks.json'))
ch, MAT = data['chunks'], data['mat']

def ptxt(c):
    return f"RIC N°{c['p']} {MAT[str(c['p'])]}. {c['h']}. Sección {c['s']}\n{c['t']}"

def emb(texts):
    body = json.dumps({'model': 'nvidia/nemotron-3.5-embed-1b', 'input': texts, 'input_type': 'passage', 'encoding_format': 'float', 'dimensions': DIM, 'truncate': 'END'})
    for k in range(8):
        r = subprocess.run(['curl', '-s', '--max-time', '6', 'https://integrate.api.nvidia.com/v1/embeddings', '-H', f'Authorization: Bearer {KEY}', '-H', 'Content-Type: application/json', '-d', '@-'], input=body, capture_output=True, text=True)
        try:
            return [x['embedding'] for x in json.loads(r.stdout)['data']]
        except Exception:
            print('reintento', r.stdout[:200]); time.sleep(1 + k)
    sys.exit('falló')

cache = f'{D}/vec_f32.json'
# la API falla con lotes > 1 texto: uno por llamada, 4 hilos, ~36 por minuto
import threading
from concurrent.futures import ThreadPoolExecutor
V = json.load(open(cache)) if os.path.exists(cache) else {}
V = {int(k): v for k, v in V.items()} if isinstance(V, dict) else {}
lock, last = threading.Lock(), [0.0]
def job(i):
    with lock:
        w = last[0] + 1.55 - time.time()
        if w > 0: time.sleep(w)
        last[0] = time.time()
    v = emb([ptxt(ch[i])])[0]
    with lock:
        V[i] = v
        if len(V) % 25 == 0:
            json.dump(V, open(cache, 'w')); print(len(V), '/', len(ch), flush=True)
with ThreadPoolExecutor(3) as ex:
    list(ex.map(job, [i for i in range(len(ch)) if i not in V]))
json.dump(V, open(cache, 'w'))
V = [V[i] for i in range(len(ch))]

# normaliza y cuantiza a int8 (escala común 127 sobre vectores unitarios)
U = [[x / (math.sqrt(sum(y * y for y in v)) or 1) for x in v] for v in V]
S = 127 / max(abs(x) for u in U for x in u)
q = bytearray()
for u in U:
    q += bytes((round(x * S) & 0xFF) for x in u)
open(f'{D}/out/vec.bin', 'wb').write(bytes(q))
idx = {'dim': DIM, 'scale': S, 'mat': MAT, 'url': data['url'], 'c': [[c['p'], c['s'], c['h'], c['pg'], c['t']] for c in ch]}
json.dump(idx, open(f'{D}/out/ric.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print('ok', len(q), 'bytes vec', os.path.getsize(f'{D}/out/ric.json'), 'bytes json')
