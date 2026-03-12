import informacio

for i in range(13):
 print(f"Paciente {i+1}")
 informacio.agregarNombre()
 informacio.guardarEdad()
print("-------NOMBRES:---")
informacio.imprimirNombres()
print("-------EDADES:---")
informacio.imprimirEdades()
print("----COMPARACION---")
informacio.comparacion()