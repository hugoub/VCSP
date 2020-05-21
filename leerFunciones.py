#!/usr/bin/env python
# -*- coding: cp1252 -*-

def leerShift():
    datos=open("Datos/datosShift.txt",'r')
    ini=datos.readline()
    inicio=eval(ini)
    med=datos.readline()
    medio=eval(med)
    fin=datos.readline()
    final=eval(fin)
    datos.close()
    return inicio,medio,final

def leerShiftIni():
    datos=open("Datos/datosShiftIni.txt",'r')
    ini=datos.readline()
    inicio=eval(ini)
    datos.close()
    return inicio

def leerShiftMid():
    datos=open("Datos/datosShiftMid.txt",'r')
    med=datos.readline()
    medio=eval(med)
    datos.close()
    return medio

def leerShiftFin():
    datos=open("Datos/datosShiftFin.txt",'r')
    fin=datos.readline()
    final=eval(fin)
    datos.close()
    return final
    
def leerInstancia():
    datos=open("Datos/instancia.txt",'r')
    dep=datos.readline()
    d=eval(dep)
    arr=datos.readline()
    a=eval(arr)
    sta=datos.readline()
    s=eval(sta)
    end=datos.readline()
    e=eval(end)
    tim=datos.readline()
    t=eval(tim)
    tdep=datos.readline()
    tDep=eval(tdep)
    cos=datos.readline()
    c=eval(cos)
    cin=datos.readline()
    cIn=eval(cin)
    cou=datos.readline()
    cOut=eval(cou)
    trip=datos.readline()
    cTrip=eval(trip)
    datos.close()
    return d,a,s,e,t,tDep,c,cIn,cOut,cTrip

def leerSolucionSin():
    datos=open("Datos/solucionSinH.txt","r")
    x1=datos.readline()
    xOut=eval(x1)
    x2=datos.readline()
    x=eval(x2)
    x3=datos.readline()
    xIn=eval(x3)
    trip=datos.readline()
    y=eval(trip)
    datos.close()
    return xOut,x,xIn,y


def leerSolucionCon():
    datos=open("Datos/solucionConH.txt","r")
    x1=datos.readline()
    xOut=eval(x1)
    x2=datos.readline()
    x=eval(x2)
    x3=datos.readline()
    xIn=eval(x3)
    trip=datos.readline()
    y=eval(trip)
    datos.close()
    return xOut,x,xIn,y    
               
def leerTripulacion():
    datos=open("Datos/tripulaciones.txt","r")
    trip=datos.readline()
    y=eval(trip)
    return y
