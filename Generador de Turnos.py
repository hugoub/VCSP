#!/usr/bin/env python
# -*- coding: cp1252 -*-

# Program: Assignment Model
# por Hugo Ubilla

from leerFunciones import *
from instancia import *
import time

#Ejemplos
start = time.time()

N=range(len(d))
K=len(tDep)        #Número de depósitos

tMax=4*60  #Tiempo Max. de conducción
tDesc=2*60  #Tiempo de descanso
tMaxTurno=8*60  #Tiempo máximo de turno


#Tiempo depósito a viajes

par=[]

#Creación de Grafo Dirigido con servicios factibles

#1) En este caso sirve cuando es necesario que la estacion de llegada y salida sean las mismas
'''
for i in range(len(d)):
    par.append([])
    for j in range(len(d)):
        if a[i]<=d[j]:
            if e[i]==s[j]:
                par[i].append(1)
            else:
                par[i].append(0)
        else:
            par[i].append(0)
'''
#2) En este caso no (se toma el tiempo entre estaciones)

for i in range(len(d)):
    par.append([])
    for j in range(len(d)):
        if a[i]+t[e[i]][s[j]]<=d[j]:
            par[i].append(1)
        else:
            par[i].append(0)


# print par

##########Busqueda de caminos

union=[]
for i in range(len(d)):
    union.append([])
    for j in range(len(d)):
        if par[i][j]==1 and (d[j]-d[i]<=tMax):
            union[i].append(j)

def agregar(viaje,nivel,principal):
    u=[]
    for j in range(len(union[viaje])):
        if (d[union[viaje][j]]-d[principal]>=tMax):
            break
        aux=ruta[nivel]
        n=aux[:]
        ruta.append(n)
        ruta[-1].append(union[viaje][j])
        u.append(len(ruta)-1)
    for k in u:
        agregar(ruta[k][-1],k,principal)


# CREACIÓN DE LOS RECORRIDOS

# Sección 1: #Matrices de todos los recorridos posibles empezando en una estación

p=[]    #p es el conjunto de todos los recorridos factibles sin descanso
for j in range(len(d)):
    ruta=[[j]]
    agregar(j,0,j)
    p=p+ruta

#print p    #Matriz con todos los recorridos posibles sin descanso

# Sección 2: #Matrices de todos los recorridos posibles empezando por un depósito

pDepI=[]
pDepIni=[]

#Para cada depósito se duplica p. Para cada viaje se le agrega un depósito a pDepI

for i in range(K):
    for j in range(len(p)):
        pDepI=p[j][:]
        pDepIni.append(pDepI)
        pDepIni[j+len(p)*i].insert(0,len(d)+i)

#print pDepIni #Recorridos con nodo inicial como depósito



# Sección 3: #Matrices de todos los recorridos posibles terminando por un depósito

pDepF=[]
pDepFin=[]

for i in range(K):
    for j in range(len(p)):
        pDepF=p[j][:]
        pDepFin.append(pDepF)
        pDepFin[j+len(p)*i].insert(len(d),len(d)+i)

#print pDepFin #Recorridos con nodo final como depósito



# Sección 4: #Matrices de todos los recorridos posibles empezando y terminando por un depósito
#PODRÍA SER OMITIDO SI JUNTAMOS 2 Y 3

pDepT=[]
pDepTod=[]

for i in range(K):
    for j in range(len(p)):
        pDepT=p[j][:]
        pDepTod.append(pDepT)
        pDepTod[j+len(p)*i].insert(0,len(d)+i)
        pDepTod[j+len(p)*i].insert(len(d),len(d)+i)

#print pDepTod #Recorridos con nodo inicial y final como depósito



#***************************************************************************************
#CREACIÓN DE LOS SPELL

#Duración por viaje


largo=[]
duracion=[]


#1.- Función creacionSpell: encargada de crear los spell de acuerdo a los recorridos.

def creacionSpell(recorrido):
    spell=[]
    for i in range(len(recorrido)):
        r=len(recorrido[i])
        spell.append([])
        horaInicio=0
        for j in range(r):
            if recorrido[i][0]>=len(d) and recorrido[i][-1]<len(d):
                if j==0 and (a[recorrido[i][1]]-(d[recorrido[i][1]]-tDep[recorrido[i][0]-len(d)][recorrido[i][1]]))<tMax:
                    spell[i].append(recorrido[i][j])
                    horaInicio=d[recorrido[i][1]]-tDep[recorrido[i][0]-len(d)][recorrido[i][1]]
                if j>0:
                    if (a[recorrido[i][j]]-horaInicio)<tMax:
                        spell[i].append(recorrido[i][j])
            if recorrido[i][r-1]>=len(d) and recorrido[i][0]<len(d):
                if recorrido[i][j]>=len(d):
                    if (a[recorrido[i][j-1]]+tDep[recorrido[i][j]-len(d)][recorrido[i][j-1]]-d[recorrido[i][0]])<tMax:
                        spell[i].append(recorrido[i][j])
                elif (a[recorrido[i][j]]-d[recorrido[i][0]])<tMax:
                    spell[i].append(recorrido[i][j])
            if recorrido[i][r-1]<len(d) and recorrido[i][0]<len(d):
                if (a[recorrido[i][j]]-d[recorrido[i][0]])<tMax:
                    spell[i].append(recorrido[i][j])
    #Eliminacion de duplicados
    spe=[]
    for i in range(len(spell)):
        if spell[i] not in spe and spell[i]!=[]:

            spe.append(spell[i])
    spell=spe
    return spell


#2.- Función largoSpell: Encargada de obtener el largo (Hora de Fin menos Hora de Inicio) de cada spell.

def largoSpell(recorrido):
    for i in range(len(recorrido)):
        r=len(recorrido[i])
        if recorrido[i][0]>=len(d) and recorrido[i][r-1]<len(d):
            largo.append((a[recorrido[i][r-1]]-d[recorrido[i][1]]-tDep[recorrido[i][0]-len(d)][recorrido[i][1]]))
        if recorrido[i][r-1]>=len(d) and recorrido[i][0]<len(d):
            largo.append((a[recorrido[i][r-2]]+tDep[recorrido[i][r-1]-len(d)][recorrido[i][r-2]]-d[recorrido[i][0]]))
        if recorrido[i][r-1]<len(d) and recorrido[i][0]<len(d):
            largo.append((a[recorrido[i][r-1]]-d[recorrido[i][0]]))
    return largo


#print largoSpell(creacionSpell(pDepFin))


#***********************************************************************************************************************************
#CREACIÓN DE LOS SHIFT


#3.- Función creacionShift: Encargada de crear los shift.

shift=[]
descanso=[-1]    #nodo de descanso

spellIni=creacionSpell(pDepIni)
spellFin=creacionSpell(pDepFin)
spellMid=creacionSpell(p)

for j in range(len(spellFin)):
    for i in reversed(range(len(spellFin))):
        if spellFin[i][-1]<len(d):
            spellFin.pop(i)


def creacionShiftDepMid(dep,mid):
    shift=[]
    for i in range(len(mid)):
        r=len(mid[i])
        for j in range(len(dep)):
            t=len(dep[j])
            if (a[dep[j][-1]]+tDesc<d[mid[i][0]]) and ((a[mid[i][r-1]]-d[dep[j][0+1]]-tDep[dep[j][0]-len(d)][dep[j][0+1]])<=tMaxTurno) and e[dep[j][t-1]]==s[mid[i][0]]:
                shift.append(dep[j]+descanso+mid[i])
    return shift


def creacionShiftMidDep(mid,dep):
    shift=[]
    for i in range(len(dep)):
        r=len(dep[i])
        for j in range(len(mid)):
            t=len(mid[j])
            if (a[mid[j][t-1]]+tDesc<d[dep[i][0]]) and ((a[dep[i][r-2]]+tDep[dep[i][r-1]-len(d)][dep[i][r-2]]-d[mid[j][0]])<=tMaxTurno) and e[mid[j][t-1]]==s[dep[i][0]]:
                shift.append(mid[j]+descanso+dep[i])
    return shift


def creacionShiftMid(mid):
    for i in range(len(mid)):
        r=len(mid[i])
        for j in range(len(mid)):
            t=len(mid[j])
            if (a[mid[i][r-1]]+tDesc<d[mid[j][0]]) and ((a[mid[j][t-1]]-d[mid[i][0]])<=tMaxTurno) and e[mid[i][r-1]]==s[mid[j][0]]:
                shift.append(mid[i]+descanso+mid[j])
    return shift


def creacionShiftDepDep(depI,depF):
    shift=[]
    for i in range(len(depF)):
        r=len(depF[i])
        for j in range(len(depI)):
            t=len(depI[j])
            if (a[depI[j][t-1]]+tDesc<d[depF[i][0]]) and ((a[depF[i][r-2]]+tDep[depF[i][r-1]-len(d)][depF[i][r-2]]-d[depI[j][0+1]]-tDep[depI[j][0]-len(d)][depI[j][0+1]])<=tMaxTurno) and e[depI[j][t-1]]==s[depF[i][0]]:
                shift.append(depI[j]+descanso+depF[i])
    return shift


#Explicación:
#1er if: la hora de llegada del spell 1 mas un descanso debe ser menor que la salida de spell 2.
#2do if: la hora de llegada del ultimo spell menos la hora de salida del primero no debe superar el largo de un turno
#3er if: la estaciones de llegada y salida deben ser las mismas
      
#*****************************************************************************************************************************************************************

#CREACIÓN DE LA FUNCION CON LOS CREW
#Creación de todos los tipos de Shift

shiMM=creacionShiftMid(spellMid)+spellMid
shiDM=creacionShiftDepMid(spellIni,spellMid)+spellIni
shiMD=creacionShiftMidDep(spellMid,spellFin)+spellFin
shiDD=creacionShiftDepDep(spellIni,spellFin)

#1.- Creación de F en MID

mid1=[]
mid2=[]
mid3=[]

#Viaje Central MID
for i in range(len(shiMM)):
    mid2.append([])
    for j in range(len(d)):
        mid2[i].append(0)

for i in range(len(shiMM)):
    for j in range(len(shiMM[i])):
        if shiMM[i][j]!=-1:
            mid2[i][shiMM[i][j]]=1

#Viaje Inicio MID
for i in range(len(shiMM)):
    mid1.append([])
    for j in range(K):
        mid1[i].append(0)

#Viaje Final MID
for i in range(len(shiMM)):
    mid3.append([])
    for j in range(len(d)):
        mid3[i].append(0)


#2.- Creación DepMid
            
depMid1=[]
depMid2=[]
depMid3=[]

#Viaje Central DEP MID
for i in range(len(shiDM)):
    depMid2.append([])
    for j in range(len(d)):
        depMid2[i].append(0)

for i in range(len(shiDM)):
    for j in range(len(shiDM[i])):
        if shiDM[i][j]!=-1 and j!=0 and j!=1:
            depMid2[i][shiDM[i][j]]=1


#Viaje Inicio DEP MID
for i in range(len(shiDM)):
    depMid1.append([])
    for j in range(K):
        depMid1[i].append(0)

for i in range(len(shiDM)):
    depMid1[i][shiDM[i][0]-len(d)]=shiDM[i][1]+1

#Viaje Fin DEP MID
for i in range(len(shiDM)):
    depMid3.append([])
    for j in range(len(d)):
        depMid3[i].append(0)

#3.- Creación MidDep

midDep1=[]
midDep2=[]
midDep3=[]

#Viaje Central MID DEP
for i in range(len(shiMD)):
    midDep2.append([])
    for j in range(len(d)):
        midDep2[i].append(0)

for i in range(len(shiMD)):
    r=len(shiMD[i])
    for j in range(len(shiMD[i])):
        if shiMD[i][j]!=-1 and j!=r-1:
            midDep2[i][shiMD[i][j]]=1

#Viaje Inicio MID DEP
for i in range(len(shiMD)):
    midDep1.append([])
    for j in range(K):
        midDep1[i].append(0)

#Viaje Fin DEP MID
for i in range(len(shiMD)):
    midDep3.append([])
    for j in range(len(d)):
        midDep3[i].append(0)

for i in range(len(shiMD)):
    midDep3[i][shiMD[i][-2]]=shiMD[i][-1]-len(d)+1

#*****************************************************************************************************************************************************************
#Unión de Funciones!

#1.- Todos los shift
shiftTotal=shiMM+shiMD+shiDM

#2.- Matrices de Inicio
inicio=mid1+midDep1+depMid1

#3.- Matrices de Medio
medio=mid2+midDep2+depMid2

#4.- Matrices de Fin
final=mid3+midDep3+depMid3

