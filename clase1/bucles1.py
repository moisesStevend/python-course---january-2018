import time

edad=0
adm =True

try:
	while (edad<8) and (adm==True):
		print("edad es: ", edad)
		edad+=1
		time.sleep(0.5)
except:	
	print("sali por un error")


a=[6,7,85,47,8]

for x in a:
	print(x)

