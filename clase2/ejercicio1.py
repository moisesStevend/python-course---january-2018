#ingrese por teclado un texto
#y retornar solo las consonantes

#lambda
#funciones inline

#menos de 5 lineas.

############## funcion #############################
cons = lambda x,v: [i for i in x if not(i in v)]
####################################################


ingreso = input("ingrese: ") 
vocales="aeiou"
my_cons = cons(ingreso, vocales)

