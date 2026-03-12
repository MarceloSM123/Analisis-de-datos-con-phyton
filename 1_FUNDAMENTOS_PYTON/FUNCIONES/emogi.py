def encontrarPalabra(frase):
    if "feliz" in frase:
        print(f"El emogi que te representa es : \U0001F600")
    elif "triste" in frase:
        print(f"El emogi que te representa es : \U0001F641")  

lista=[]
def agregarFrase(frase):
    lista.append(frase)
    print(f"la frase fue guardada correctamente: {lista}")