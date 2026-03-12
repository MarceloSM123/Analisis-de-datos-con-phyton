#METODOS ESTATICOS

from laptop import laptop
laptopPepito=laptop("lenovo", "intel i7", "100gb", 1000, 120)
laptopMaria=laptop("dell", "intel i79", "10gb", 100, 120)
print(laptopPepito.__dict__)
print(laptopPepito.valorFinal())
print(laptopPepito.valorDescuento(10))
#llamada la metodo estatico
print(laptop.compararCosto(laptopPepito,laptopMaria))
#Llamada a metodo de clase
for numero in range(1,1001):
    asusLaptop=laptop.asusLaptop(numero)
    print(asusLaptop.__dict__)