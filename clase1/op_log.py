#operadores logicos

a=bin(10)	# 0b1010
print(a)

b=bin(6)	# 0b0110
print(b)

print(10&6)	# result : 2

#aplicando mascaras
mask=4		# 0b0100
print("6 and 4: ",6&4)
print("desplazado 2: ", (6&4)>>2)
