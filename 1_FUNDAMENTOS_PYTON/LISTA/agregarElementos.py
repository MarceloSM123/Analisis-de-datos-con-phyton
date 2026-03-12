#agregar lementos a una lista
lista=[1,2,3,4,5]
print(lista)
lista.append(6) #agrega un elemento al final de la lista, de izquierda a derecha
print(lista)
lista.insert(2,"Marcelo") #inserta elementos en la lista en una ubicacion dada
print(lista)
lista.extend([6,7,8,9]) #encadena la lista original con la lista dada
print(lista)
lista2=[6,7,8,9]
lista3=lista+lista2 #encadena las listas nombradas con sus respectivos elementos
print(lista3)