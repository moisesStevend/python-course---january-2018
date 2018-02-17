#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 10:47:40 2018

@author: stevend

Introducciona Herencia en POO
"""
#################################################
class Humano():    
    def __init__(self, nombre=''):
        self.nombre = nombre
        self.__apellido="Meza" #atributo privado
        print("init de Humano")
        
    def hablar(self, text=''):
        print(self.nombre,"dice: ",text)
    
    def __pensar(self):
        print("pensando")
    
    def set_apellido(self, nA):
        self.__apellido = nA
    
    def get_apellido(self):
        return self.__apellido
        
################################################3333
class Programador(Humano):
    def __init__(self,nombre):
        print("init de Programador")
        #super(Programador, self).__init__(nombre)
        #super(self.__class__, self).__init__(nombre)
        super(Programador, self).__init__(nombre)
        
    def programar(self, leng=''):
        print("programo en ",leng)    
#################################################
class Matematico():
    _pi = 3.1416       #variables de clases
    
    def __init__(self):
        self.pref = None
    
    def aritmetica(self, argum=''):
        #self.pref = 'aritmetica'
        return "estudio aritmetica"
    
    def algebra(self, argum=''):
        #self.pref = 'algebra'
        return "estudio algebra"
    
    def geometria(self, argum=''):
        #self.pref = 'geometria'
        return "estudio geometria"
        
    def trigonometria(self, argum=''):
        #self.pref = 'trigonometria'
        return "estudio trigonometria"
    
    def preferencia(self, pref=''):
        d={
            'aritmetica': self.aritmetica(),
            'algebra': self.algebra(),
            'geometria': self.geometria(),
            'trigonometria': self.trigonometria()
            }  
        self.pref = pref
        #print('pref: ',pref, 'd[pref]',d[pref], 'self.pref',self.pref)
        return d[pref]  
################################################
if __name__ == '__main__':
    Matematico._pi = 101.70
    
    pitagoras = Matematico()
    r = pitagoras.preferencia('aritmetica')
    pitagoras.pref = 'geometria'
    print('pita:',r)
    print('pita:',pitagoras.pref)
    pitagoras._pi=12
    print('pita:', pitagoras._pi)
    
    
    euler = Matematico()
    rr = euler.preferencia('algebra')
    euler.pref = 'trigonometria'
    print('euler:',rr)
    print('euler:',euler.pref)
    print('euler: ',euler._pi)
    
    '''
    Daniel = Programador('Daniel')
    Daniel.hablar("hola")
    Daniel.nombre="Juan"
    Daniel.hablar("hi")
    Daniel.set_apellido("Rodriguez")
    ape = Daniel.get_apellido()
    print(ape)
    
    '''
        

