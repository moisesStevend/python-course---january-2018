import time
import sys

trun = int(input("ingrese truncamiento: "))#20
pares=[]

for x in range(101):#[0:100]
	if x==0 or x==1:
		pass
	elif x%2==0:
		if x==trun:
			continue
		pares.append(x)
		#print("es par: ",x)
		#
		#
		#

print(pares)	
print(trun in pares)
print("termino el codigo")

