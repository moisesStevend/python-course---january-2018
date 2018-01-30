#funcion con *args

def my_list(p1, p2, *p):
	#p: es una tupla
	sumar=p1+p2
	
	otra_suma=0	
	for i in p:
		otra_suma+=i
			
	print(sumar+otra_suma)
	#print(p,type(p))


my_list(5,6,7,8,9)
