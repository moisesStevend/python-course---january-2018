#funcion de funcion

def datos(*args,**kwargs):	
	global a
	
	a='inline'
	
	def potencias(*args,**kwargs):
		cuad=[]
		for i in args:
			cuad.append(i**kwargs['pot'])
		return cuad
	
	if kwargs['hab']:	#==True
		return potencias(*args,**kwargs)
		
	else:
		return "no esta habilitado"	

result = datos(3,4,5, pot=3, hab=False)
print(result)

print(a)
