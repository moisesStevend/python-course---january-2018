#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:27:30 2018

@author: stevend
"""

class Operaciones():
    def __init__(self,a,b):
        self.a=a   #self.a es un atributo de la clase Oper
        self.b=b
    
    def sumar(self, x=1,y=3):
        print('self.a: ',self.a)
        return x+y
    
    def restar(self, x,y, *args, **kwargs):
        return x-y
    

op = Operaciones(78,90)      #instanciamos la clase
r = op.sumar(4,5)
print(r)

rr = op.restar(9,5)
print(rr)

print('atributo self.a: ',op.a)