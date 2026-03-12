nombrePaciente=[]
edad=[]


def agregarNombre():
    nombre=input("Ingrese el nombre del paciente: ")
    apellido=input("Ingrese el apellido del paciente: ")
    nombrePaciente.append(nombre+" "+apellido)

def guardarEdad():
    añoNacimiento =int(input("ingrese el año de nacimiento del paciente: "))
    edadPersona=2026-añoNacimiento
    edad.append(edadPersona)

def imprimirNombres():
    print(nombrePaciente)

def imprimirEdades():
    print(edad)

def comparacion():
    indiceMax=edad.index(max(edad))
    print(f"El paciente con mas edad es {nombrePaciente[indiceMax]} tiene {max(edad)}")
    indiceMin=edad.index(min(edad))
    print(f"El paciente mas joven es {nombrePaciente[indiceMin]} tiene {min(edad)}")