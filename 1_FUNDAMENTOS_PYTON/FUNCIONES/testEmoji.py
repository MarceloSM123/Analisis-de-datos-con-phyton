import emogi

cantidadFrase=input("Cuantas frases desea ingresar: ")
for i in range(int(cantidadFrase)):
    frase=input("Ingrese la frase")
    emogi.encontrarPalabra(frase)
    emogi.agregarFrase(frase)