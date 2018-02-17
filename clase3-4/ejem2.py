# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:00:07 2018
@author: stevend
"""
#funciones
#funciones sin retorno

def quita_vocal(s="",n=1):
    l=[i for i in s if not(i in "aeiou")]
    l=''.join(l)    #junta str de un lista
    print l*n       #print ("curso de "+s)*n

quita_vocal("python",1)   #print "curso de "+"python"
quita_vocal("spyder",1)
quita_vocal("labotec")
try:
    quita_vocal(45,2)
except:
    #print "****error de argumentos****"
    pass

#funciones con retorno
import math

def sumar(x=0,y=0):
    s=x+y
    return s

def senoidal(ang=10):
    return math.sin(ang*math.pi/180)

def r_2vlue():
    a,b=12,45
    return a,b

p = sumar(3,4)
print p

g=senoidal(30)
print g

t,q = r_2vlue()
print t,q 

#gestion de funciones
def my_func(a,b,*args,**kwargs):#parametros
    print 'a',a, type(a)
    print 'b',b, type(b)
    print 'args',args, type(args)
    print 'kwargs',kwargs, type(kwargs)
#funcion con argumentos
my_func(9,8,5,6,7,dist=90, alt=15)

#variables globales y locales en funciones
a=20

def restar(x,y,aa):
    print aa+1
    aa=34
    s=x-y 
      
    global ff
    ff=34    
    return s


restar(20,10,a)
print(ff)

#funciones anonimas
def multiplicar1(x,y):
    '''
        mas codigo
    '''
    s=x*y
    return s

#funcion lambda
multiplicar2 = lambda x,y: x*y

print multiplicar1(3,4)
print multiplicar2(5,7)

#map, filter, reduce, funciones d funciones
#decoradores, generadores

#funciones de orden superior
def saludar(lang):
    def saludar_es():
        print "hola"
    def saludar_en():
        print "hello"
    def saludar_fra():
        print "wi"
    a=12
     
    selec = {
        'es': saludar_es,
        'en': saludar_en,
        'fra': saludar_fra
    }
    
    return selec[lang]   
    #return saludar_es, a

f = saludar('es')
f("python")
#print p
    
    
    
    
    
    
    
    
    




































































