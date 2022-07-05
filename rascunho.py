from collections import deque
import numpy as np

x = "_"
estado_inicial = "2_3541687"
#estado_inicial = deque(estado_inicial)
"""
#esquerda
#estado_inicial.rotate(-1)
#print(estado_inicial)
#direita
estado_inicial.rotate(1)
print(estado_inicial)

#estado_inicial.swap(1,3)
#print(estado_inicial)

i = estado_inicial.find("_")
estado_inicial = list(estado_inicial)
aux = estado_inicial[i]
aux2 = estado_inicial[i+3]
estado_inicial[i] = aux2
estado_inicial[i+3] = aux
print(estado_inicial)
"""

def esquerda(estado):
    i = estado.find("_")
    estado = list(estado)
    if(i-1 < 0):
        aux = estado[i]
        aux2 = estado[len(estado)]
        estado[i] = aux2
        estado[len(estado)] = aux

        
        
    else:
        aux = estado[i]
        aux2 = estado[i-1]
        estado[i] = aux2
        estado[i-1] = aux
        estado = ''.join(estado)
    return str(estado)


def direita(estado):
    i = estado.find("_")
    estado = list(estado)
    if(i+1 > len(estado)):
        aux = estado[i]
        aux2 = estado[0]
        estado[i] = aux2
        estado[0] = aux

        
        
    else:
        aux = estado[i]
        aux2 = estado[i+1]
        estado[i] = aux2
        estado[i+1] = aux
        estado = ''.join(estado)
    return str(estado)

print(direita(estado_inicial))