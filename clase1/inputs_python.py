#!/usr/bin/env python3
# inputs en python

try:
	valor = int(input("ingrese valor: "))	#el error puede ocurrir aqui
	print(valor)
	print(type(valor))
	print(valor + 2)
except:
	print("hubo error")

print("pero sigue corriendo el codigo")
