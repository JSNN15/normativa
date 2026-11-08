"""Corta los 19 pliegos RIC en fragmentos por sección numerada, con página, para búsqueda semántica."""
import re, json, glob, os, sys
D = os.path.dirname(os.path.abspath(__file__))
MAT = {1: 'Empalmes', 2: 'Tableros eléctricos', 3: 'Alimentadores y demanda de una instalación',
       4: 'Conductores, materiales y sistemas de canalización', 5: 'Medidas de protección contra tensiones peligrosas y descargas eléctricas',
       6: 'Puesta a tierra y enlace equipotencial', 7: 'Instalaciones de equipos', 8: 'Sistemas de emergencia',
       9: 'Sistemas de autogeneración', 10: 'Instalaciones de uso general', 11: 'Instalaciones especiales',
       12: 'Instalaciones en ambientes explosivos', 13: 'Subestaciones y salas eléctricas',
       14: 'Eficiencia energética en edificios', 15: 'Infraestructura para la recarga de vehículos eléctricos',
       16: 'Subsistemas de distribución', 17: 'Operación y mantenimiento', 18: 'Presentación de proyectos', 19: 'Puesta en servicio'}
URLS = {int(re.search(r'RIC-N(\d+)', u).group(1)): u for u in open(f'{D}/raw/urls.txt').read().split() if 'RIC-N' in u}
HEAD = re.compile(r'^\s{0,10}(\d{1,2}(?:\.\d{1,2}){0,4})\.?\s{2,}([A-ZÁÉÍÓÚÑa-záéíóúñ¿"“(].*)$')
ANX = re.compile(r'^\s{20,}(ANEXO\s+(?:N°\s*)?\d+\.\d+)\.?\s*$')
FOOT = re.compile(r'(Pliego Técnico Normativo RIC|SEC\s*-\s*División de Ingeniería|P\s*á\s*g\s*i\s*n\s*a\s+\d|^\s*\d+\s*$)')
TARGET, MAXC = 1300, 2000

def clean(s):
    return re.sub(r'[ \t]{2,}', '  ', s).strip()

def parse(path, n):
    pages = open(path, encoding='utf-8').read().split('\f')
    secs = []  # (num, title, page, lines)
    cur = {'n': '0', 't': 'Encabezado', 'pg': 1, 'L': []}
    top = 0
    for pi, pg in enumerate(pages, 1):
        for ln in pg.split('\n'):
            if FOOT.search(ln) or '.....' in ln:
                continue
            m = HEAD.match(ln)
            if m:
                num, txt = m.group(1), m.group(2).strip()
                first = int(num.split('.')[0])
                # rechaza filas de tablas: el primer componente no puede saltar lejos del capítulo actual
                if top - 1 <= first <= top + 1 or (top == 0 and first == 1):
                    if '.' not in num:
                        top = first
                    secs.append(cur)
                    cur = {'n': num, 't': txt, 'pg': pi, 'L': [ln]}
                    continue
            a = ANX.match(ln)
            if a:
                secs.append(cur); top = 99
                cur = {'n': a.group(1).upper().replace('  ', ' '), 't': a.group(1), 'pg': pi, 'L': [ln]}
                continue
            cur['L'].append(ln)
    secs.append(cur)
    return secs

def title_of(sec):
    t = sec['t']
    return t if len(t) < 90 else ''

def build():
    chunks = []
    for path in sorted(glob.glob(f'{D}/txt/RIC-N*.txt')):
        n = int(re.search(r'RIC-N(\d+)', path).group(1))
        secs = parse(path, n)
        titles = {}  # número -> título corto (capítulos y secciones)
        for s in secs:
            t = title_of(s)
            if t and s['n'].count('.') <= 1 and ':' not in t and not t.endswith(',') and len(t) < 75:
                titles.setdefault(s['n'], t.rstrip('.'))
        buf, start = [], None

        def flush():
            nonlocal buf, start
            if not buf:
                return
            text = '\n'.join(clean(x) for x in '\n'.join(b['txt'] for b in buf).split('\n') if x.strip())
            text = re.sub(r'\n{2,}', '\n', text)
            if len(text) > 80:
                s0 = buf[0]
                ch = s0['n'].split('.')[0]
                sub = '.'.join(s0['n'].split('.')[:2])
                path_t = ' › '.join(x for x in [titles.get(ch, ''), titles.get(sub, '') if sub != ch else ''] if x)
                # parte largas en trozos sin cortar palabras
                parts, rest = [], text
                while len(rest) > MAXC:
                    cut = rest.rfind('\n', 0, TARGET + 300)
                    if cut < TARGET // 2:
                        cut = rest.rfind(' ', 0, TARGET + 300)
                    parts.append(rest[:cut]); rest = rest[cut:].lstrip()
                parts.append(rest)
                for pi, p in enumerate(parts):
                    chunks.append({'p': n, 's': s0['n'] + ('' if buf[-1]['n'] == s0['n'] else '–' + buf[-1]['n']),
                                   'h': path_t, 'pg': s0['pg'], 't': p})
            buf, start = [], None

        for s in secs:
            if s['n'] == '0':
                continue
            txt = '\n'.join(s['L'])
            key = '.'.join(s['n'].split('.')[:2])
            size = sum(len(b['txt']) for b in buf)
            if buf and (size + len(txt) > TARGET or (key != start and size > 600) or key.split('.')[0] != start.split('.')[0]):
                flush()
            if start is None:
                start = key
            buf.append({'n': s['n'], 'pg': s['pg'], 'txt': txt})
        flush()
    # página real de cada trozo: busca su comienzo en el texto de cada página
    pages = {}
    for path in glob.glob(f'{D}/txt/RIC-N*.txt'):
        n = int(re.search(r'RIC-N(\d+)', path).group(1))
        pages[n] = [re.sub(r'\s+', ' ', pg) for pg in open(path, encoding='utf-8').read().split('\f')]
    for i, c in enumerate(chunks):
        c['id'] = i
        probe = re.sub(r'\s+', ' ', c['t'])[:50]
        for k in range(c['pg'] - 1, len(pages[c['p']])):
            if probe in pages[c['p']][k]:
                c['pg'] = k + 1; break
    return chunks

if __name__ == '__main__':
    ch = build()
    json.dump({'mat': MAT, 'url': URLS, 'chunks': ch}, open(f'{D}/chunks.json', 'w'), ensure_ascii=False)
    L = [len(c['t']) for c in ch]
    print(len(ch), 'fragmentos', sum(L), 'car', 'max', max(L), 'prom', sum(L) // len(L))
    from collections import Counter
    print(Counter(c['p'] for c in ch))
    for c in ch[::max(1, len(ch) // 6)]:
        print('---', c['p'], c['s'], c['h'], 'pág', c['pg']); print(c['t'][:300])
