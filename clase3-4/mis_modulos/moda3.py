#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 09:23:17 2018

@author: stevend

Hallar la moda, y si existen varios 
encontrarlos.
"""
#ingreso de lista
#hallar los numeros repetidos

#l=[4,5,6,3,3,6,6,8,8,86,4,3,6,5]

__author__  = "Moises Stevend Meza Rodriguez"
__credits__ = "labotec"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "moises.stevend@gmail.com" 
__status__  = "Developer"

class Moda():
    def __init__(self):
        """
        metodo inicialde seteo de atributos
        
        """
        self.moda=None     #atributos
        self.count=0        #atributos
        self.camb=None
        self.max=1

    def get_moda(self,li):
        """
            metodo que sirve pra hallar la moda
            
            li es una lista:
                ejm: li=[38484,585,86,4,3,34]
            
        """
        li.sort()       #modo ordenado
        self.camb=li[0] #3
        #print(li)
        for i in li:    #recorra toda la lista
            #print(i)
            if i==self.camb:    #si se repite
                 #print('i:_',i)
                 self.count+=1  #cuente las repeticiones
                 #print('ii:',i,'count: ',self.count, 'camb:',self.camb, 'i: ',i)
                 #self.camb=
            else:  #si no se repite
                #print(i)
                if self.max<self.count:
                    self.max=self.count
                    self.moda=self.camb               
                    #print('max: ',self.max, 'moda: ',self.moda, 'camb',self.camb)
                self.camb=i
                self.count=0
            
        return self.moda, self.max

if __name__ == '__main__':
    l=[4,5,6,3,3,6,6,8,8,86,4,3,6,3,6,6,6,6,6,6,3,4,4,4,4,4,5]
    
    mo = Moda()
    mi_moda = mo.get_moda(l)
    print(mi_moda)
    
                    
                        
        


