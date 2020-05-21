#!/usr/bin/env python
# -*- coding: cp1252 -*-

# Program: Assignment Model
# por Hugo Ubilla

from pulp import * #  LP modeler written in python
from Shift import *
from instancia import *

# Orientación del problema

vcsp = LpProblem("Vehicle and Crew Scheduling Model",LpMinimize)

# Parámetros

L=range(len(inicio))        #Cantidad de tripulaciones
N=range(len(d))             #Cantidad de viajes
H=range(len(cOut))          #Cantidad de depósitos

#Cantidad de buses por depósito
v=[]
for i in H:
    v.append(15)

#Creación de conjuntos de viajes compatibles
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

x = LpVariable.matrix('x',(N,N,H),0,1,LpInteger)
xOut = LpVariable.matrix('xOut',(H,N),0,1,LpInteger)
xIn = LpVariable.matrix('xIn',(N,H),0,1,LpInteger)
y = LpVariable.matrix('y',(L),0,1,LpInteger)


# Función objetivo

z = lpSum([lpSum([lpSum([x[i][j][h]*c[i][j][h] for i in N]) for j in N]) for h in H]) + lpSum([lpSum([cOut[h][j]*xOut[h][j] for j in N]) for h in H]) + lpSum([lpSum([cIn[i][h]*xIn[i][h] for i in N]) for h in H]) + lpSum([y[l]*cTrip for l in L])

# función objetivo

vcsp += z

# Restricciones

for i in N:
    vcsp += lpSum([lpSum([x[i][j][h] for j in fin[i]]) for h in H]) + lpSum([xIn[i][h]for h in H]) == 1

for j in N:
    vcsp += lpSum([lpSum([x[i][j][h] for i in ini[j]]) for h in H]) + lpSum([xOut[h][j] for h in H]) == 1

for i in N:
    for h in H:
        vcsp += xIn[i][h] + lpSum([x[i][j][h] for j in fin[i]]) - xOut[h][i] - lpSum([x[j][i][h] for j in ini[i]]) == 0

for h in H:
    vcsp += lpSum([xOut[h][j] for j in N]) <= v[h]

for j in N:
    for h in H:
        vcsp += xOut[h][j]-lpSum([y[l]*inicio[l][h][j] for l in L]) == 0
        
for j in N:
    vcsp += lpSum([lpSum([x[i][j][h] for i in ini[j]]) for h in H]) - lpSum([y[l]*medio[l][j] for l in L]) == 0

for h in H:
    for j in N:
        vcsp += xIn[j][h]-lpSum([y[l]*final[l][j][h] for l in L]) == 0

# Escribir modelo
vcsp.writeLP("ModeloVCSPflotahomogenea.lp")

# Solving
vcsp.solve(CPLEX())


# Values
s = []
for i in N:
    s.append([])
    for j in N:
        s[i].append([])
        for h in H:
            s[i][j].append(x[i][j][h].value())

sIn = []
for i in N:
    sIn.append([])
    for h in H:
        sIn[i].append(xIn[i][h].value())

sOut = []
for h in H:
    sOut.append([])
    for i in N:
        sOut[h].append(xOut[h][i].value())

sTrip = []
for l in L:
    sTrip.append(y[l].value())


z = value(vcsp.objective)

print z

resultado=open("Datos/solucionSinH.txt","w")
resultado.write(str(sOut)+"\n")
resultado.write(str(s)+"\n")
resultado.write(str(sIn)+"\n")
resultado.write(str(sTrip)+"\n")

resultado.write(str(z)+"\n")

'''
print '**************************'
print 'La solución es xIn: '
print sIn
print 'La solución es: xOut'
print sOut
print 'La solución es: X'
print s
print 'La solución es: Y:'
print sTrip
print 'La función objetivo es: ',z

'''
