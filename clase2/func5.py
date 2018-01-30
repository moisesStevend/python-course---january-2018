#funcion con **kwargs

'''
def varios(p1,p2,p3,**kwargs):
	print(p1)
	print(p2)
	print(p3)
	print(kwargs, type(kwargs))

varios('a', 2.3, 12, value=35, otro=2,a=56)
'''

def my_func(value1, value2, *args, **kwargs):
	print("parametros definidos:")
	print(value1,value2)
	
	print("parametros extras *args")
	for i in args:
		print(i)
	
	#for i in kwargs.items():
	#	print(i[1])
	print("parametros extras en **kwargs")
	for i in kwargs.values():
		print(i)	

my_func(3,4,99,77,88,30,value=30)
'''
	cod1
'''

'''
	cod2
'''
my_func(1,45,56,v=56)
'''
	cod3
'''
my_func(1,45,56,v=56)
