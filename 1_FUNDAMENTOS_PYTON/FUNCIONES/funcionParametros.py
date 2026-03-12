def datos(nombre,apellido,edad,mensaje="hola"):#mensaje="hola" si el usuario no ingresa el mensaje se envia el mensaje hola por defecto
  #los parametros opcionales van al final
    if edad<18:
        print(f"{mensaje} {nombre}{apellido} es menor de edad")
    else:
        print(f"{mensaje} {nombre}{apellido} es mayor de edad") 