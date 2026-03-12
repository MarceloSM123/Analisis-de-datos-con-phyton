datos=[]
extension=int(input("Ingrese el tamaño de la lista: "))

for i in range(extension):
    datos.append(input(f"ingrese el elmento {i+1} de la lista: "))
    if datos[i].isdigit():
     print(f"El elemento {i+1} ingresado es Entero")
    elif  ((datos[i].replace('.', '', 1)).replace('-', '', 1)).isdigit():
       print(f"El elemento  {i+1} ingresado es decimal")
    else:
       print(f"El elemento {i+1} ingresado es un String")

print(f"Su lista es: {datos}")