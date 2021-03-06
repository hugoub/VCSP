#!/usr/bin/env python
# -*- coding: cp1252 -*-

# Programa: Creador de Instancia en Gams
# por Hugo Ubilla

from instancia import *
from Shift import *
N=len(penal)
D=len(v)
L=len(inicio)
V=len(v[0])

def tablaDim2(A,B,matriz,s,t):
    #A:Largo dimension 1
    #B:Largo dimension 2
    #C:Largo dimension 3
    #s:Valor inicial de espacios
    #t:valor central de espacios
    a=""
    b="".ljust(t)
    for i in range(A):
        for u in range(B):
            a=a+str(matriz[i][u]).ljust(s)
            if i==0:
                b=b+str(u+1).ljust(s)
                if u==B-1:
                    parametros.write(b+str('\n'))
            if u==B-1:
                parametros.write(str(i+1).ljust(t)+a+str('\n'))
                a=""

def tablaDim3(A,B,C,matriz,s,t):
    #A:Largo dimension 1
    #B:Largo dimension 2
    #C:Largo dimension 3
    #s:Valor inicial de espacios
    #t:valor central de espacios
    a=""
    b="".ljust(t)
    for i in range(A):
        for j in range(B):
            for u in range(C):
                a=a+str(matriz[i][j][u]).ljust(s)
                if i==0 and j==0:
                    b=b+str(u+1).ljust(s)
                    if u==C-1:
                        parametros.write(b+str('\n'))
                if u==C-1:
                    parametros.write(str(str(i+1)+"."+str(j+1)).ljust(t)+a+str('\n'))
                    a=""


parametros = open("parametrosHeterogeneo.gms","w")

parametros.write("SETS\n")
parametros.write('i estaciones /1*'+str(N)+'/\n')
parametros.write('h depositos /1*'+str(D)+'/\n')
parametros.write('l tripulaciones /1*'+str(L)+'/\n')
parametros.write('u vehiculos /1*'+str(V)+'/\n')
parametros.write('alias(i,j);\n\n\n')

parametros.write("\nTABLE penal(i,j,u) penalizaciones al medio\n")
tablaDim3(N,N,V,penal,8,12)

parametros.write("\nTABLE v(h,u) capacidad\n")
tablaDim2(D,V,v,10,12)

parametros.write("\nTABLE c(i,j,h) costos\n")
tablaDim3(N,N,D,c,8,12)

parametros.write("\nTABLE cout(h,j) costos de salida\n")
tablaDim2(D,N,cOut,8,12)

parametros.write("\nTABLE cin(i,h) costos de entrada\n")
tablaDim2(N,D,cIn,8,12)

parametros.write("\nTABLE inicio(l,h,j) tripulacion al inicio\n")
tablaDim3(L,D,N,inicio,8,12)

parametros.write("\nTABLE medio(l,j) tripulacion al medio\n")
tablaDim2(L,N,medio,8,12)
                            
parametros.write("\nTABLE final(l,j,h) tripulacion al final\n")
tablaDim3(L,N,D,final,8,12)

parametros.write("\nTABLE ini(j,i) conjunto inicio\n")
tablaDim2(N,N,ini,8,12)
                            
parametros.write("\nTABLE fin(i,j) conjunto fin\n")
tablaDim2(N,N,fin,8,12)
                            
parametros.write('\nSCALARS\n')
parametros.write(str("ctrip salario de un tripulacion /")+str(cTrip)+str("/;"))


