############## creacion de funcion #############
def print_list(val=[1,2,3]):	#val: se llama parametro
	try:
		print("rango:")
		for i in val:	
			print(i,'ok')
		print('\n')
	except:
		print("ingrese otra var, no se puede recorrer")
	
##########################
'''
	otro codigo1
'''

a=[3,4,57,890,2]
print_list(a)	# a: se llama argumento

#########################
'''
	otro codigo2
'''
b=[12,34,55,77,88]
print_list(b)	# b: se llama argumento

#########################
try:
	print_list(True)
except:
	print("error")
