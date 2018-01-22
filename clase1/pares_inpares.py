import time

varTop = int(input("hallando los pares hasta: "))

for x in range(1,(varTop+1)):
	if x==1:
		pass
	elif x%2==0:
		print("es par  ",x)
	else:
		print("es impar", x)
