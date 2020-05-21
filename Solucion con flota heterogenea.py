#!/usr/bin/env python
# -*- coding: cp1252 -*-

# Program: Assignment Model
# por Hugo Ubilla

from leerFunciones import *

xOut,x,xIn,y=leerSolucionCon()
trip=leerTripulacion()

salida=[]
viaje=[]
aux=0
for a in range(len(xOut)):
    for b in range(len(xOut[a])):
        for c in range(len(xOut[a][b])):
            if xOut[a][b][c]==1:
                salida.append([])
                salida[aux].append(a)
                salida[aux].append(b)
                salida[aux].append(c)
                viaje.append(b)
                aux=aux+1
print "Salidas:\n",salida

entrada=[]
aux=0
for a in range(len(xIn)):
    for b in range(len(xIn[a])):
        for c in range(len(xIn[a][b])):
            if xIn[a][b][c]==1:
                entrada.append([])
                entrada[aux].append(a)
                entrada[aux].append(b)
                entrada[aux].append(c)
                aux=aux+1

print "Entradas:\n",entrada


def ruta(viaje):
    global auxx
    camino[auxx].append(viaje)
    for i in range(len(x[0])):
        for a in range(len(x[0][0])):
            for b in range(len(x[0][0][0])):
                if x[viaje][i][a][b]==1:
                    ruta(i)

camino=[]
auxx=0
for a in viaje:
    camino.append([])
    ruta(a)
    auxx=auxx+1

print "Caminos:\n",camino


for a in range(len(y)):
    if y[a]==1:
        print trip[a]





                
