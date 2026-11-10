// Ejemplos de demostración: imagen, crédito y licencia de cada caso.
const SAMPLES = [
  {
    "q": "¿Cuál es el valor máximo de resistencia de puesta a tierra de servicio?",
    "qv": "f/bW8kMxAQ8SwDrP+/Esxye+Ekbi889H3Pn98/ULKusYJtwpCSQkAA4R2vXv4+8P/Sf8DD0UCC0iQvv+EfxF2fDb2/gGDA35H/YRBAwQ/PABHBEI9wPnNjH8C/oU2h3r7gwE8hkaJiFq1j3t8QUky9YF3jcb8hf3Pyf7C9AC1c/5Idf87/z61Cnq6AMo80nvCwgx2tcv28beCOHaDOXTBf8p/wunxTvq/SH09BgJzijR3Af93zg1RTkMI8ke4/5A3ib4C8UFIAne+PM7zA4M9wP5ARXy4RzLOeca3fwy+joE4xQN9J/oDCw255vg5+D98CP65/YtFsJHEuYK9xfnRBYrA/wv6hDvQOkEDeTu1+r+0+kC+QXX4dz0FQUW4/PqEtEgAdUXzDPP/xsKDALrMvzUMT0sxSX1Hv4rPADf8Po7I/Iczh0h8gfq8fEkhfzqzhHzXBfdCCDtFx41+BkSBh3iETodNeLzB/3i7ckc2vfs6QosOzAmEM/73RflyfvlDUvtrOziDjTv/Ss+5Pz/Ey8P7SrE69XV/y0LFgfvo/8U9ezW5wDQ9BTpC/zsCRdX9yL/NhPRGAAq5PkyEQkMSPAMANPm2wLFBusFBPcW+/Xs9QLLFfQ1BfzezzMFLdsxIgIb+goNKgYK4irw02UoWSUR1iMk9uLn6uALw+7/2hs=",
    "top": [
      878,
      326,
      1065,
      331,
      327,
      330
    ],
    "answer": "El valor máximo de resistencia de puesta a tierra de servicio es 20 Ohm [2], salvo que la instalación cumpla con los requisitos del punto 6.2, en cuyo caso puede superar este valor hasta 80 Ohm [5].",
    "ms": 872,
    "model": "nvidia/nemotron-3.5-lightning-30b-a3b"
  },
  {
    "q": "¿Qué exigencias tiene una sala eléctrica respecto de puertas y accesos?",
    "qv": "fw/G+AbkG+0IBhj6/gIcAPTu6xkJDAgaC+TP9A74C+ji3hzmtOrgAfsAFiAFGvTkPOgB5hohAgja2xod+gPm8wsZ1g7r/SXOFj8X+vjwEAH3ESD5+A0H+9kNHe4EFyIBDOjuATAM7vkf8yXx/xki8AME1gHnCvn08ukT/s0z9/ftKS/mAOkQzDwd8BkHABH3FP0g9Q7/JQ8VERIB4NYqGhbs6fMVHP3DDfouFwPe//ACCAvpGicH8PrtSP721ScP4PdIB/z7BgjvEfz7NOn94PH66yP6EgccG+f7+iohOgoqKPoc/w3OCPca7gf+/t7SDhTnDQz6F+hB9O0j4BAJAOv6CRwE3f//HvMD9xDvI/LtC9MUHeXlIeHUAfsN7uPVFfv9DPTz//PV+/P1ChkPCTfQDR0M8wDrFffV5PQYAgX8MQzu9u3T1QUOvOn+CPjFAQX//AoU8Ajw4ADk7wj46zDjEgAdF+Cz8A3m+9cKMAP11QxZGgcW/f0JByni8uofHkT/Ju4VA/z/BecbBfT6H/UF/fze+g8F6+EV/hQS3xErDMkNCf4AF/wPy/Xm+kD8Fv3h1eHrARP8DQLq0wYV9fIE4hLdHBsLJgr75CYU9Ogf6tcQHPUS8wIAAS4H0QYaByq93hvoBPnT+fP+CP4f7g0R5BTZ3hgeEeq9EOkJ4yI=",
    "top": [
      51,
      860,
      861,
      135,
      855,
      573
    ],
    "answer": "Las salas eléctricas deben contar con dos puertas: una de acceso de materiales y equipos y otra de servicio, siendo esta última de al menos 0,80 x 2,10 m, que se abra hacia el exterior y tenga cerradura de seguridad para apertura desde dentro sin llaves. Si el transformador cabe por la puerta de servicio, se puede omitir la de materiales. Las puertas y los recubrimientos deben ser incombustibles y está prohibido usar baldosines plásticos en subestaciones con transformadores en aceite. Verifica siempre en el pliego vigente publicado por la SEC.",
    "ms": 1280,
    "model": "nvidia/nemotron-3.5-lightning-30b-a3b"
  },
  {
    "q": "¿Qué protección exige un punto de carga de vehículo eléctrico?",
    "qv": "f/n/9REMIQXmExvN3PrxDAHpNuzi6+vQIe4YCtgN8zUIEtff4gbh9w/L5Cja9Qet9hIP2Q70/wUI3AkeGzXnD/4YBxoFyB7d3xD0FL7x/f0PNgMu8B8dAQUJJQ3LIBDq/f/nG9XqBBvx+DoGMx77runYCw0OE/Dv/O8mBtz5HvwPEE/t1gX7xijT5yIfHQ0j9/8r//cC+S8GGPMQNv/4JA/VxxEhCffk7PoLKAgHAeD1Eur4F06/LwP2I2T9/RQrGzoQMBH2sB3y/wA9B/oI9B/03gnr9gQQHbD0ERT2JwMR8jg08RnEQNUo3CDc3+bXD8j/shAMwvJQyNMmBQbo3xYUKtwF5fzmDB7qGfj/4c7W8OQ6ARryDREJPtEk0cDi7OcyKOjvzD3v8PcW/DfZ/AOw2OLd1NO8Av4XERkbLeIrCQEVF/Pz0BDZ4xoU8y7kEfXP9r8f/NwA+y7y3iMb4SPlGBsyDz6/6vPwNq/6Pso66BVYF/bT7ClCGuPiAcgJ/w4T+d4tUAfaEva33QASDR4vCVDxA9nuufz5/yIVBjUt+gHj5SwFGP73CQkpLwzXOPQD3Qr9F1vw9RTsLCz/Exsr0wztIQja8fEKABbPx/76Es/YC+Le0ub1RysARssG3QsQ9tw/KyjxIyzw1EoK00Ic6ksF/iYL993q/vYKDDE=",
    "top": [
      914,
      950,
      970,
      969,
      967,
      935
    ],
    "answer": "Un punto de carga de vehículo eléctrico exige protección diferencial de corriente con sensibilidad máxima de 30 mA, protección contra sobrecorriente según la capacidad nominal del dispositivo (10A para carga modo 1, al menos 16A para carga modo 2), y protección general con estudio de coordinación y selectividad. Además, requiere protección antivandálica y, para instalaciones exteriores, grado IP54 mínimo. Verifica siempre en el pliego vigente publicado por la SEC.",
    "ms": 1572,
    "model": "nvidia/nemotron-3.5-lightning-30b-a3b"
  },
  {
    "q": "¿Cómo se clasifican las zonas en ambientes con gases explosivos?",
    "qv": "byTo7fAqNeQ01+hUGMc2EAcE3d/Y5tzvCgLT/O7u+trX2T/W53/z7P7nNPrvJAYf5Qbs8c4V3Aoq2eQvAwDk3kH9BL7z7f0fESLVC/EH2OQD6dzw6+jjShQR/bjq9C7YAQ4xPAcSAQvl4gAo8B4X1yn+8PPRDCPr7x7u6A8Pz+8B7CTcIiM0B+4F7vrXNUfeFQYouykMvzUKJPr4F8/3B+n22twbQ9D+DxzoCfcBWfAXIQQv/vDbKjkmNvfqASrb7wEH9AHl8wwF/yYEJcsa8/z16QtJPuGbDwA9AUhGCyUjBTg4KQvR5wH2Igr67QMtKf/w7u75HuksI9YEE/gW+BkF4APvPRnvABoN1xX2MuHyB8T24NvVBhDM3h3zHf/bHyT5Ktf0HQPqzvLoAuItAOERBgf1GTPi+f35rwXwKwYdAOQuzf39ygfdsen46yb9N/YNBtbwHg4+MSk3FijY7RcT1jnzVcYG+B8FFuYjM/cP4PIa/eTyKQX1PtXD3+lK8jH6NicnANzEBzXy5lHO9uYVAxH2BNveNOnABgHzJisD8+wP6AsJBBQnAwT++P7y1gkuAvX+3wq9Gfv3+Cft5e8kBgnaFPYa7utAB/XR9hQBNP/PLRHUFgLnFSMLEb8T+EPJSC2oLgYJCuL2wkAA/O7w5Qg0DejUMf/LKL/r8xc=",
    "top": [
      823,
      804,
      801,
      821,
      794,
      796
    ],
    "answer": "Las zonas se clasifican según la presencia y duración de atmósferas explosivas: Zona 0 para presencia permanente o frecuente, Zona 1 para formación ocasional durante funcionamiento normal, y Zona 2 para atmósfera que solo subsiste por espacios de tiempo muy breves si se forma. [2][3][4] Verifica siempre en el pliego vigente publicado por la SEC.",
    "ms": 1064,
    "model": "nvidia/nemotron-3.5-lightning-30b-a3b"
  }
];
