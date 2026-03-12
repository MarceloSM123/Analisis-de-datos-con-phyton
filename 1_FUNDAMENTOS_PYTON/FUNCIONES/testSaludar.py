import saludar,funcionParametros #importamos el archivo que contiene a nuestra funcion

saludar.bienvenida() #llamamos a nuestra funcion 
funcionParametros.datos("Marcelo","Salcdedo", 33, "Bienvenido")#ingresamos los parametros segun la estructura de nuestra funcion
funcionParametros.datos("Marcelo","Salcdedo", 33)#no ingresamos el mensaje y se ejecuta el mensaje por defecto, mensaje es un parametro opcional
#podemos ingresar en desorden los parametros especificando el parametro al que pertenece la informacion ingresada
funcionParametros.datos(mensaje=" Maestro ",apellido="Salcedo",edad=33,nombre="Marcelo")