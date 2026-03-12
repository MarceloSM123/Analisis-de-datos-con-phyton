frase=input("Ingrese una frase: ")
letra=input("ingrese una letra: ")
contador=0
for i in frase:
    if i==letra:
        contador+=1
print(f"La letra {letra} se repite {contador} veces")
print(frase.count("o"))