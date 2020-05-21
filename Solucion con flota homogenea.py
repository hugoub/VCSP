#!/usr/bin/env python
# -*- coding: cp1252 -*-

# Program: Assignment Model
# por Hugo Ubilla

from leerFunciones import *

xOut,x,xIn,y=leerSolucionSin()

trip=leerTripulacion()

salida=[]
viaje=[]
aux=0
for a in range(len(xOut)):
    for b in range(len(xOut[a])):
        if xOut[a][b]==1:
            salida.append([])
            salida[aux].append(a)
            salida[aux].append(b)
            viaje.append(b)
            aux=aux+1

print salida

entrada=[]
aux=0
for a in range(len(xIn)):
    for b in range(len(xIn[a])):
        if xIn[a][b]==1:
            entrada.append([])
            entrada[aux].append(a)
            entrada[aux].append(b)
            aux=aux+1
print entrada


def ruta(viaje):
    global auxx
    camino[auxx].append(viaje)
    for i in range(len(x[0])):
        for a in range(len(x[0][0])):
            if x[viaje][i][a]==1:
                ruta(i)

camino=[]
auxx=0
for a in viaje:
    camino.append([])
    ruta(a)
    auxx=auxx+1


print camino

for a in range(len(y)):
    if y[a]==1:
        print trip[a]





                
