#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 13:06:19 2018

@author: stevend
generador se quea enla funcion 
"""
def recorrido(*args): # args=(3,4,5,67,8,56,78,1)
    for j in args:#(4,5)
        yield j**2

for i in recorrido(3,4,5,67,8,56,78,1):
    print(i)

print("termino el generador \n")
#############################################
#funcion map

r = list(map(lambda x: x**2, [1,2,3,4,5]))
print(r)

#funcion filter
rr = list(filter(lambda x: x>8, [1,2,3,4,5,6,7,8,9,10]))
print(rr)

l=[1,2,3,4,5,6,7,8,9,10]
l_aux=[]
for x in l:
    if x>8:
        l_aux.append(x)
l=l_aux
print(l)




