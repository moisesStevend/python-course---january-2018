#funciones con retorno
def sumar(x,y):
	s=x+y
	#print(s)
	
	def pares(x,y):
		print(x,y)
	
	pares(x,y)
	
	return s
	
result = sumar(3,4)
#result2 = sumar(7,8)

#print(result)
#print(result2)

print(result)
