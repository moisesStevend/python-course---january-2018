#funciones globales 
a='externo'

def my_func(x,y,ext):
	try:
		ext*=2
		print(ext)	#solo lectura
	except:
		pass
			
	global b
	b=12
	return x+y

result = my_func(3,4,a)
print(result)

b=b+2
print(b)
