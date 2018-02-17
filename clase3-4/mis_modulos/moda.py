#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:00:42 2018

@author: stevend


Suponiendo que nos suministran una 
lista de enteros, diseña una función 
que calcule su moda. La moda es el elemento
más repetido en una serie de valores

"""

l=[4,6,7,8,6,4,3,6,4,5,6,7,9,9,6,4,4,4,4,4]

d={}    #diccionario vacio

for i in l: #inicializo con valores 0
    d[i]=0
    
for i in l:  #cantidad de numeros q se repite
    d[i]+=1   #d[i]=d[i]+1

max=0
for i in d.keys(): #hallar el maximo valor
    if d[i]>max:
        max=d[i]

moda=0
for i in d.items(): #encontrar ese numero
    if max==i[1] :
        moda=i[0]

print(moda)
        
########################################################
#moda version2
l=[4,6,7,8,6,4,3,6,4,5,6,7,5,5,5,5,9,9,6,5,5,5,4,4,4,5,5,5,4,4,4,4,4]


def moda(lll):
    """
        documentacion de la fucion moda
    """
    lll.sort()       
    max_n=[lll[0],1]
    count=0
    i_ant=lll[0]
    
    for i in lll:
        if i==i_ant:    
            count+=1
        else:
            if max_n[1]<count:
                max_n=[i_ant,count]
            i_ant=i
            count=1
    return max_n

r = moda(l)

print(r)
#########################################################
#moda version3
l=[4,6,7,8,2,2,2,2,2,2,2,2,2,2,2,6,4,3,6,2,2,2,4,5,6,7,5,5,5,5,9,9,6,5,5,5,4,4,4,5,5,5,4,4,4,4,4]
l_aux=l
count_g=1
modas=[]

for i in l_aux:
    max=l[0]
    count=1
    
    for i in l_aux:
        if l_aux.count(i)>count:
            max=i
            count=l_aux.count(i)   
    
    modas.append([max,count])   
    
    l_aux = list(filter(lambda j: j!=max, l_aux))
    if count_g < count:    
        count_g=count
    else:
        break

print(modas)
                
        
    
        
        
        
        
        
        
        
        
        
        
            
    