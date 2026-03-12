#Listas
planetas=["mercurio","Venus","Tierra", "Marte"]
print(planetas[0]) #selector cuenta de izquierda a derecha
print(planetas[-1])#el selector cuenta de derecha a izquierda
print(planetas[1:3]) #impresion parcial de la lista
print(planetas[1: ]) #impresion complementaria a partir del indice dado
print(planetas[:-1]) #impresion desde los elementos izquierdos hasta llegar al indice dado
print(len(planetas)) #imprime el numero de elementos de la lista
#-------------------------------#
#Trabajar con una lista de numeros
gravedadEnPlanetas=[0.378,0.907,1,0.377 ]
pesoBus=124054 #Newtons en la tierra
print(f"En la tierra, un autobus de dos pisos pesa {pesoBus} N")
print(f"En mercurio, un autobus de dos pisos pesa {pesoBus*gravedadEnPlanetas[0]} N")
print(f"lo mas liviano que serua un autobus en el sistema solar es {pesoBus*min(gravedadEnPlanetas)} N") #la funcion min devuelve el valor minimo de la lista
print(f"el peso maximo que alcanza en el sistema solar es {pesoBus*max(gravedadEnPlanetas)} N") #la funcion max devuelve el valo maximo de la lista

