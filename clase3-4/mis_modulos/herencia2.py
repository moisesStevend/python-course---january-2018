#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:34:35 2018

@author: stevend
"""
class Humano():
    def __init__(self):
        self.p = '' #None
        
    def hablar(self, text=''):
        print(text)
    
    def pensar(self):
        self.p='estoy pensando'
        
class Cantante():
    def componer(self, cancion=''):
        print("mi canciones ", cancion)

class Ingeniero(Humano, Cantante):
    def planificar(self, plan=''):
        self.mensj='ing'
        print("panificar", plan)

if __name__ == "__main__":
    eliot = Ingeniero()        
    eliot.planificar('viaje espacial ')
    
    try:
        assert eliot.mensj=='otra cosa'
    except Exception as e:
        print(e)
    
    eliot.hablar("hola soy ingeniero")
    eliot.componer("mi auto era una rana")
    
    eliot.pensar()
    print(eliot.p)