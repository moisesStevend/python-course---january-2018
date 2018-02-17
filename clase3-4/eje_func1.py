#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 15:17:34 2018

@author: stevend
"""
#funciones sin retorno
def add_lastName(s='',n=1):
    r=s*n
    print(r)

add_lastName("labotec",3)

#gestionar los argumentos de la funcion
def show_f(a=1,b=0,c=2,*args,**kwargs):#int, int,int, tuple, dict
    print(a,b,c,type(a))
    print(args,type(args))
    print(kwargs,type(kwargs))
    
show_f(2,3,5,9,7,5,0,data=23, temp=30)

#funciones con retorno
def sumar(x=0,y=0, *args, **kwargs):
    return x+y

r = sumar(3,4)
print(r)

#funciones de orden superior
def operaciones(x,y,op,op1):
    def sumar(x,y):
        return x+y
    def restar(x,y):
        return x-y
    def dividir(x,y):
        return x/y
    
    mi_op={
            'sumar': sumar(x,y),
            'restar': restar(x,y),
            'dividir': dividir
            }
    
    mi_op1={
            'sumar': sumar(x,y),
            'restar': restar(x,y),
            'dividir': dividir
            }
        
    return mi_op1[op],mi_op[op1]

rr = operaciones(5,3,'dividir','sumar')
print(rr(9,3))

#funciones anonimas
#funcion lambda
l=['h','o','l','a'] 

def l2s(ll,n=1):
    return (''.join(ll))*n #join junta los elementos de lista

r = l2s(l,2)
print(r, type(r))

#funcion lambda
l2s2 = lambda ll,n=1: (''.join(ll))*n

rr = l2s2('labotec')
print(rr)

#comprension de listas
k=[1,2,3,4,5,6,7]
kk=range(1,8)  #[1,2,3,4,5,6,7]
print(kk)

p=[i for i in range(1,20+1) if (i%2==0)]
print(p)

#recordar
l=[]
l.append(4)   #agregar valores a una lista

d={}
d.update(data='censo', temp=30) #update a data en dict


def others1(a,b,c):
    print('a: ',a)
    print('b: ',b)
    print('c: ',c)

def others2(a,b,c, *args, **kwargs):
    print('a: ',a)
    print('b: ',b)
    print('c: ',c)
    print('*args:', args)

others1(b=90,c=58,a=4)
others2(90,58,4, 6, 7, 8)



'''
Diseña un programa que, dados cinco números enteros, 
determine cuál de los cuatro últimos números es más 
cercano al primero. 
(Por ejemplo, si el usuario 
introduce los números 2, 6, 4, 1 y 10, 
el programa responderá que el número más
cercano al 2 es el 1.)
'''

#a=1,4,5,6
#raw_input
#input


a=[3,16,9,8,26]

def cercano(l):#l=[3,16,9,8,26]
    c=l[1] #16
    dmin=abs(l[0]-c)   #abs(3-16) --> 13
    
    for i in l[2:]:
        if abs(l[0]-i)<dmin:
            dmin=abs(l[0]-i)  #6
            c=i
    return c

r = cercano(a)
print(r)
















































