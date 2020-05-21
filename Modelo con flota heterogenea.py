#!/usr/bin/env python
# -*- coding: cp1252 -*-

# Program: Modelo VCSP con prioridad según tipo de vehículo
# por Hugo Ubilla

from pulp import *
from instancia import *
from Shift import *

# Orientación del problema

vcsp = LpProblem("Vehicle and Crew Scheduling Models",LpMinimize)

# Parámetros

L=range(len(inicio))        #Cantidad de tripulaciones
N=range(len(d))             #Cantidad de viajes
H=range(len(cOut))          #Cantidad de depósitos

k=len(v[0])         #Tipos de buses
                    #0: Mediano - 1: Grande
U=range(k)                  #Cantidad de tipos de buses

#Construcción de conjuntos de viajes compatibles
fin=[]
ini=[]
for i in N:
    fin.append([])
    ini.append([])

for i in N:
    for j in N:
        if a[i]+t[e[i]][s[j]]<=d[j]:
            fin[i].append(j)
            ini[j].append(i)




# Variables

x = LpVariable.matrix('x',(N,N,H,U),0,1,LpInteger)
xOut = LpVariable.matrix('xOut',(H,N,U),0,1,LpInteger)
xIn = LpVariable.matrix('xIn',(N,H,U),0,1,LpInteger)
y = LpVariable.matrix('y',(L),0,1,LpInteger)

# Función objetivo
z = lpSum([lpSum([lpSum([lpSum([x[i][j][h][u]*c[i][j][h]*penal[i][j][u] for i in N]) for j in N]) for h in H]) for u in U]) + lpSum([lpSum([lpSum([cOut[h][j]*xOut[h][j][u] for j in N]) for h in H]) for u in U]) + lpSum([lpSum([lpSum([cIn[i][h]*xIn[i][h][u] for i in N]) for h in H]) for u in U])+ lpSum([y[l]*cTrip for l in L])

vcsp += z


# Restricciones

for i in N:
    vcsp += lpSum([lpSum([lpSum([x[i][j][h][u] for j in fin[i]]) for h in H]) for u in U]) + lpSum([lpSum([xIn[i][h][u] for h in H]) for u in U]) == 1

for j in N:
    vcsp += lpSum([lpSum([lpSum([x[i][j][h][u] for i in ini[j]]) for h in H]) for u in U]) + lpSum([lpSum([xOut[h][j][u] for h in H]) for u in U]) == 1
    
for i in N:
    for h in H:
        for u in U:
            vcsp += xIn[i][h][u] + lpSum([x[i][j][h][u] for j in fin[i]]) - xOut[h][i][u] - lpSum([x[j][i][h][u] for j in ini[i]]) == 0

for h in H:
    for u in U:
        vcsp += lpSum([xOut[h][j][u] for j in N]) <= v[h][u]

for j in N:
    for h in H:
       vcsp += lpSum([xOut[h][j][u] for u in U])-lpSum([y[l]*inicio[l][h][j] for l in L])== 0

for j in N:
    vcsp += lpSum([lpSum([lpSum([x[i][j][h][u] for i in ini[j]]) for h in H])for u in U])- lpSum([y[l]*medio[l][j] for l in L]) == 0

for j in N:
    for h in H:
        vcsp += lpSum([xIn[j][h][u] for u in U])-lpSum([y[l]*final[l][j][h] for l in L]) == 0

# Escribir modelo
vcsp.writeLP("ModeloVCSPflotaheterogenea.lp")

# Resolver
vcsp.solve(CPLEX())

# Tomar valores
s = []
for i in N:
    s.append([])
    for j in N:
        s[i].append([])
        for h in H:
            s[i][j].append([])
            for u in U:
                s[i][j][h].append(x[i][j][h][u].value())

sIn = []
for i in N:
    sIn.append([])
    for h in H:
        sIn[i].append([])
        for u in U:
            sIn[i][h].append(xIn[i][h][u].value())

sOut = []
for h in H:
    sOut.append([])
    for i in N:
        sOut[h].append([])
        for u in U:
            sOut[h][i].append(xOut[h][i][u].value())

sTrip = []
for l in L:
    sTrip.append(y[l].value())

z = value(vcsp.objective)

print z

#Escritura de resultados en archivo externo

resultado=open("Datos/solucionConH.txt","w")
resultado.write(str(sOut)+"\n")
resultado.write(str(s)+"\n")
resultado.write(str(sIn)+"\n")
resultado.write(str(sTrip)+"\n")

resultado.write(str(z)+"\n")

