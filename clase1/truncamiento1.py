import time
import sys

trun = int(input("ingrese truncamiento: "))

for x in range(101):#[0:100]
	if x==0 or x==1:
		pass
	elif x%2==0:
		#par
		if x<(trun+1):
			print("es par: ",x)
		else:
			break
			#sys.exit()
			
print("termino el codigo")
