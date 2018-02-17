# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:55:06 2018

@author: stevend
"""

'''
esto es un comentario
'''
# '""'

a=12            #entero
type(a)         #tipo de dato
print isinstance(a,int)

f=12.3           #flotante
c=1+6j           #complejo
s="hola mundo"   #string
b1=True         #booleano
b2=False        #booleano

#colecciones
s="python para todos"       #string
l=[45, 67.4, 'web', True]   #listas
t=(45, 67.4, 'web', True)   #tuplas
# list()  convierte a lista una tupla
# tuple() convierte una lista a tupla

l=[]    #lista vacia
t=()    #tupla vacia

l1=[3]  #lista unitaria
t1=(2,) #tupla unitaria

l1.append(3)  #insertar valores 
# 'h' in 'hola'  si pertenece

d={'data': 24, 'temp':45, 34: 'es un bool'}
# d.keys()    obtienes los keys
# d.values()  obtienes los valores
# d.items()   obtienes los keys y valores

# condicionales
if ('h' in 'hola') and (d['data']==34):
    print "es correcto"
elif d['temp']==45:
    print "d[temp] es 45, correcto"
else:
    print "nada es correcto"

# bucle for-in
l=[6,5,3,2,7]
s="python para todos"
vocales="aeiou"

for i in s:
    if not(i in vocales):
        if i=='p':
            continue    #salta a la sig. iterac
        elif i=='d':
            break       #mata al bucle for
        else:
            print i

print "sali del for"

#bucle while
x=0
x_pass=[3,9]
while x<10:
    if not((x%2==0)) and x!=0:
        if not(x in x_pass):       
            x+=1
            continue
        elif x==9:
                break
        else:
            print 'correcto: ',x
    x+=1

print "termino con exito"
#conversiones
# f = raw_input("") ingreso por teclado
# int('45')
# float('3.1416')
# str(45)
# bool(1) ---> True, bool(0) --> False

#sintaxis pythonicas
o=range(10) # [0,1,2,3,4,5,6,7,8,9]
o2=range(3,10)  #[3,4,5,6,7,8,9]

#ejemplos del factorial
lf = int(raw_input("limite de factorial: "))
aux=1
for i in range(1,lf+1):
    aux=aux*i

print "factorial es: "+str(aux)

#generar listas inline
#modo tradicional
pares=[]
for i in range(1,100+1):
    if i%2==0:
        pares.append(i)
print pares

#modo pythonico, puntual y sencillo
p=[i for i in range(1,101) if i%2==0]

















