#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:50:11 2018

@author: stevend

Haz un programa que pida el valor de dos enteros n y m 
y calcule el sumatorio de todos los números pares
comprendidos entre ellos (incluyéndolos en el caso 
de que sean pares).
"""

def show_f():
    print("soy una funcion")

class Sumatoria():
    def __init__(self,min=0,max=10):
        self.n=min
        self.m=max
    
    def sumandos(self, op):
        def g_sumatoria(x,y):
            aux=0
            for i in range(x,y+1):
                aux+=i
            
            return aux
        
        def g_sumatoriaC(x,y):
            aux=0
            for i in range(x,y+1):
                aux+=i**2
            
            return aux
        
        def suma_pares(x,y):
            aux=0
            for i in range(x,y+1):
                if i%2==0:
                    aux+=i
            
            return aux
        
        selector = {
                'suma': g_sumatoria(self.n, self.m),
                'sumac': g_sumatoriaC(self.n, self.m),
                'sumap': suma_pares(self.n, self.m)
                }
        
        #return g_sumatoria(self.n,self.m)
        return selector[op] 

if __name__ == '__main__':
    obj = Sumatoria(3,10)
    r_s = obj.sumandos('sumap')
    print(r_s)