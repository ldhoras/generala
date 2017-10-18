#!usr/bin/env python3
#-*-coding:utf-8;-*-
#V 1.1

import random
import sys
import os
import pdb

def tira(nro):
    b=[]
    for n in range(nro):
        b.append(random.randint(1,6))
    return(b)

def comando():
    global fgJuego   
    fgJuego=True
    cmd=input('Comando: ')
    if len(cmd)>1:
        pass
    elif cmd=="f" or cmd=='s':
        sys.exit(0)   #sale del programa
    elif cmd=="t":
        printTabla()   #imprime la tabla de puntaje
    elif cmd=="p":
        pass   #pone el valor elegido en memoria

def totales(total):
    global jugador
    global tabla
    if tabla[11][jugador+1]!='':
        a=int(tabla[11][jugador+1]) + total
        tabla[11][jugador+1]= str(a)
    else:
        tabla[11][jugador+1]=str(total)
   

def eligePuntaje(puntaje):
    global jugador
    global tabla
    pnt=puntaje.split('x')
    #pdb.set_trace() #@@@
    if len(pnt)==2:
        tabla[int(pnt[1])-1][jugador+1]=pnt[0]
        totales(int(pnt[0]))
    elif puntaje=='e':
        tabla[6][jugador+1]='20'
        totales(20)
    elif puntaje=='0e':
        tabla[6][jugador+1]='0'       
    elif puntaje=='es':
        tabla[6][jugador+1]='25'
        totales(25)
    elif puntaje=='f':
        tabla[7][jugador+1]='30'
        totales(30)
    elif puntaje=='0f':
        tabla[7][jugador+1]='0'       
    elif puntaje=='fs':
        tabla[7][jugador+1]='35'
        totales(35)
    elif puntaje=='p':
        tabla[8][jugador+1]='40'
        totales(40)
    elif puntaje=='ps':
        tabla[8][jugador+1]='45'
        totales(45)
    elif puntaje=='0p':
        tabla[8][jugador+1]='0'       
    elif puntaje=='g':       
        tabla[9][jugador+1]='50'
        totales(50)
    elif puntaje=='0g':
        tabla[9][jugador+1]='0'       
    elif puntaje=='2g':
        tabla[10][jugador+1]='100'
        totales(100)
    elif puntaje=='02g':
        tabla[10][jugador+1]='0'

def cargaTabla(nro):
    global tabla
    linea=[]
    for k in range (nro+1):
        linea.append('')
    for k in range(12):
        tabla.append(linea[:])
    i=0
    for k in ('1','2','3','4','5','6','E','F','P','G','2G','T'):
        tabla[i][0]=k
        i+=1

def printTabla(nro):
    i=0
    global encabezado
    global tabla
    for nombre in encabezado:
        if nombre=='N':
            print('%s' % nombre.rjust(2),end="")
        else:
            print('%s' % nombre.rjust(6),end="")
    print()
    for i in range(12):
        primer=True
        j=0
        for valor in tabla[i]:
            if j==0:
                print('%s' % tabla[i][j].rjust(2),end="")
                j+=1
            else:
                print('%s' % tabla[i][j].rjust(6),end="")
                j+=1
        print()

def errores(p,total):
    '''Controla que los numeros elegidos sean validos'''   
    tt=[]
    for n in range(5):
        tt.append(total[n])
    for i in p:
        for j in total:
            try:
                if int(i)==j:
                    tt.remove(j)
                    break
            except:
                break
    if len(tt)+len(p)!=5:
        return True
    else:
        return False

def controlPuntaje(p):
    condicion=False
    altos='0e,e,es,f,fs,0f,p,ps,0p,g,0g,2g,02g'
    sp=p.split('x')
    if len(p)==0:
        condicion=True
    elif p.count('x') != 0 and p.count('x') != 1:
        condicion=True
    elif p.count('x') == 1 and sp[0].isnumeric() and sp[1].isnumeric():
        if int(sp[1]) < 1 or int(sp[1])>6:
            condicion=True
        else:
            if int(sp[0]) % int(sp[1]) != 0:
                condicion=True
            if tabla[int(sp[1])-1][jugador+1]!='':
                condicion=True
    elif altos.count(p)==0:
        condicion=True
    return condicion

def valorFalso(pje,tiro):
    global jugador
    condicion=True
    ac=0
    try:
        sp=pje.split('x')
        for i in range(5):
            if int(sp[1])==tiro[i]:
                ac=ac+tiro[i]
            if ac==int(sp[0]):
                condicion=False
                break
            else:
                condicion=True
        #pdb.set_trace() #Acá está el (pdb)
                   
    except:
        tr=sorted(tiro)
        if pje=='g' or pje=='2g':
            if tr.count(tr[0])==5:
                condicion=False
        elif pje=='p' or pje=='ps':
            if tr.count(tr[0])==4 or tr.count(tr[1])==4:
                condicion=False
        elif pje=='f' or pje=='fs':
            if (tr.count(tr[0])==3 and tr.count(tr[4])==2) or (tr.count(tr[0])==2 and tr.count(tr[4])==3):
                condicion=False
        elif pje=='e' or pje=='es':
            e1=[1,2,3,4,5]
            e2=[2,3,4,5,6]
            e3=[1,3,4,5,6]
            if tr==e1 or tr==e2 or tr==e3:
                condicion=False              
        elif  pje=='0e' or pje=='0f' or pje=='0p' or pje=='0g' or pje=='02g':
            condicion=False
    return condicion   
   
def juego(nom):
    global fgJuego
    global jugador
    global nro

    fgJuego=True
    while fgJuego==True:
        print('juega %s: ' % nom ,end="")
        #jugar=input(nom) #acá está el nombre que se debe sacar
        jugar=input()
        if jugar=='c':
            comando()
        else:
            fgJuego=False
    fgJuego=True
    primerTiro=tira(5)
    #print('juega: %s' % nom)
    print(primerTiro)
    for k in range(2):
        erro=True
        while erro==True:
            print(nom,'elige y tira: ' ,end="")
            deNuevo=input()
            if deNuevo=='n':
                deNuevo=""
                for i in range(5):
                    deNuevo=deNuevo + str(primerTiro[i])
            if deNuevo=='c':
                comando()
            else:
                fgJuego=False
            fgJuego=True
            erro=errores(deNuevo,primerTiro)
        cantNuevos=len(deNuevo)
        a=5
        j=0
        for i in range(cantNuevos):
            while j < a:
                if int(deNuevo[i]) == primerTiro[j]:
                    del primerTiro[j]
                    j=a
                    a-=1
                else:
                    j+=1
            j=0
        segTiro=tira(cantNuevos)
        primerTiro=primerTiro+segTiro
        print(primerTiro)
        if k==1:
            os.system('clear')
            printTabla(nro)
            print(primerTiro)
            err1=True
            while err1==True:
                print(nom, 'elija el puntaje: ',end='')
                pJuego=input()
                if pJuego=='c':
                    comando()
                    break
                err1= controlPuntaje(pJuego)
                err2 = valorFalso(pJuego,primerTiro)
                if err2==True:
                    err1=err2
           
            os.system('clear')
            eligePuntaje(pJuego)
            printTabla(nro)
            #os.system('clear')

fgJuego=True
tabla=[]
encabezado=['N']
nro=1
jugadores=[]
nroJugadores=0
jugador=0

print('entre los nombres:\n(f para finalizar)')
fg=True
while (True):
    entr=input('Jugador: ')
    if entr==''or entr=='f':
        os.system('clear')
        break
    jugadores.append([nro,entr])   
    encabezado.append(jugadores[nro-1][1])
    nro+=1
nroJugadores=jugadores[-1][0] #numero de jugadores
cargaTabla(nroJugadores)
printTabla(nro)
n = -1
while(True):
    n+=1
    if n==nroJugadores:
        n=-1
        jugador=0
    else:
        jugador=jugadores[n][0]-1
        juego(jugadores[n][1])
