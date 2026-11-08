"""Correcciones manuales sobre out/ric.json: tablas que pdftotext desordena.
Cada parche reemplaza el texto de un fragmento por la tabla escrita en filas, igual al PDF oficial."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
PARCHES = {
    (6, 'ANEXO 6.7'): (
        "ANEXO 6.7\nDIMENSIONAMIENTO DE LA SECCION MINIMA DEL CONDUCTOR DE TIERRA DE PROTECCION.\n"
        "La sección del conductor de puesta a tierra de protección se fijará de acuerdo con la siguiente tabla.\n"
        "Tabla: sección de los conductores de fase S (mm²) → sección mínima de los conductores de protección correspondientes (mm²)\n"
        "S ≤ 25 → S (la misma sección que la fase)\n25 < S ≤ 50 → 25\nS > 50 → S/2\n"
        "S: es el valor de la sección de la fase.\n"
        "Nota: Esta tabla es aplicable solamente a conductores de cobre, para otro tipo de conductores la sección del "
        "conductor de tierra de protección será igual a la sección del conductor de fase."),
}
j = json.load(open(f'{D}/out/ric.json'))
for c in j['c']:
    if (c[0], c[1]) in PARCHES:
        c[4] = PARCHES[(c[0], c[1])]
json.dump(j, open(f'{D}/out/ric.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print('parches aplicados')
