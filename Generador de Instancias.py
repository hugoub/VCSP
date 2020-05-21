#!/usr/bin/env python
# -*- coding: cp1252 -*-

# Programa: Generador de instancias
# por Hugo Ubilla

import time
from random import *

'''
#Tamaño de la instancia
N=raw_input("Inserte la cantidad de viajes:\n")       #Cantidad de Viajes
while N.isdigit()==False:
    print "Por favor, inserte un valor correcto\n"
    print "-------------------------------------\n"
    N=raw_input("Inserte la cantidad de viajes:\n")
    
E=raw_input("Inserte la cantidad de estaciones:\n")    #Cantidad de Estaciones
while E.isdigit()==False:
    print "Por favor, inserte un valor correcto\n"
    print "-------------------------------------\n"
    E=raw_input("Inserte la cantidad de viajes:\n")
    
D=raw_input("Inserte la cantidad de depósitos:\n")    #Cantidad de Depósitos
while D.isdigit()==False:
    print "Por favor, inserte un valor correcto\n"
    print "-------------------------------------\n"
    D=raw_input("Inserte la cantidad de viajes:\n")

print "---------------------------- O -----------------------------\n"
'''

N=5     #Número de viajes
E=2     #Número de estaciones
D=2     #Número de depósitos
k=2     #Tipos de buses
            #0: Chico - 1: Grande


U=range(k)                  #Cantidad de tipos de buses

start = time.time()

#Horas de Salida
d=[]
for i in range(N):
    d.append(randrange(8*60,23*60,10)) #randrange(min, max, saltos)
                                       #Empieza a las 6 y termina a las 23 h

aux=0
for i in range(N):
    for j in range(N-1):
        if d[j]>d[j+1]:
            aux=d[j]
            d[j]=d[j+1]
            d[j+1]=aux


#Horas de llegada
a=[]
for i in range(N):
    a.append(randrange(d[i]+30,d[i]+3*60,20)) #Un viaje debe durar min 20 min y máximo 4 horas

#Estación de salida de cada viaje
s=[]
for i in range(N):
    s.append(randrange(0,E))

#Estación de arribo de cada viaje
e=[]
for i in range(N):
    e.append(randrange(0,E))

#Tiempo entre estaciones
t=[]
for i in range(E):
    t.append([])
    for j in range(E):
        t[i].append(randrange(20,41,10))

for i in range(E):
    for j in range(E):
        t[i][j]=t[j][i]         #Matriz triangular
        if (i==j):
            t[i][j]=0           #Diagonal


#Tiempo entre depositos y estaciones
tiDepEst=[]
for i in range(D):
    tiDepEst.append([])
    for j in range(E):
        tiDepEst[i].append(randrange(0,41,10))


#Tiempo entre depositos y viajes
tDep=[]
for i in range(D):
    tDep.append([])
    for j in range(N):
        tDep[i].append(tiDepEst[i][s[j]])


#Costos viajes Intermedios
c=[]
for i in range(N):
    c.append([])
    for j in range(N):
        c[i].append([])
        for h in range(D):
            c[i][j].append((t[e[i]][s[j]]+(a[j]-d[j]))*1000)


#Costos viajes Salida
cOut=[]
for h in range(D):
    cOut.append([])
    for i in range(N):
        cOut[h].append(randrange(150000,151000,1000))
        cOut[h][i]=cOut[h][i]+tDep[h][i]*1000

        
#Costos viajes arribo
cIn=[]
for i in range(N):
    cIn.append([])
    for h in range(D):
        cIn[i].append(tDep[h][i]*10000)

#Costo de Tripulaciones (Todas cobran lo mismo)
'''
cTrip=[]
for i in range(N):
    cTrip.append([])
    for l in range(N):
        cTrip[i].append(1000000)
'''
cTrip=1000000

end = time.time()

print end-start

# Parámetros

v=[]                        #Cantidad de tipos de buses por depósito
for i in range(D):
    v.append([])
    for u in U:
        v[i].append(200)


#Construcción de conjuntos de viajes compatibles
fin=[]
ini=[]
for i in range(N):
    fin.append([])
    ini.append([])
    for j in range(N):
        fin[i].append([])
        fin[i][j]=0
        ini[i].append([])
        ini[i][j]=0

for i in range(N):
    for j in range(N):
        if a[i]+t[e[i]][s[j]]<=d[j]:
            fin[i][j]=1
            ini[j][i]=1

#Penalización en horarios punta
#Todos los buses que salgan entre las 7 a las 9 y de 18 a 20
#Buses grandes en horario normal y buses medianos en horario punta estan penalizados

         
penal=[]
for i in range(N):
    penal.append([])
    for j in range(N):
        penal[i].append([])
        for u in range(k):
            penal[i][j].append(1)
            

for i in range(N):
    for j in range(N):
        for u in range(k):
            if u==0 and ((d[j] >= 7*60 and d[j] < 9*60) or (d[j] >= 18*60 and d[j] < 20*60)):
                penal[i][j][u]=1.05
            if u==1 and ((d[j] >= 6*60 and d[j] < 7*60) or (d[j] >= 9*60 and d[j] < 18*60) or (d[j] >= 20*60 and d[j] < 23*60)):
                penal[i][j][u]=1.05

#Archivo Externo
instancia = open("instancia.py","w")
instancia.write("d="+str(d)+"\n")
instancia.write("a="+str(a)+"\n")
instancia.write("s="+str(s)+"\n")
instancia.write("e="+str(e)+"\n")
instancia.write("t="+str(t)+"\n")
instancia.write("tDep="+str(tDep)+"\n")
instancia.write("penal="+str(penal)+"\n")
instancia.write("v="+str(v)+"\n")
instancia.write("c="+str(c)+"\n")
instancia.write("cIn="+str(cIn)+"\n")
instancia.write("cOut="+str(cOut)+"\n")
instancia.write("cTrip="+str(cTrip)+"\n")
instancia.write("ini="+str(ini)+"\n")
instancia.write("fin="+str(fin)+"\n")
instancia.close()

