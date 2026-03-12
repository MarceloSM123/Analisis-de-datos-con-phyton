#METODOS ESTATICOS
from laptop import laptop
from laptopGaming import laptopGaming
from LaptopBusiness import laptopBusiness

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
laptopGa=laptopGaming("MSI", "intel i7", 4, "RTX 8GB")
print(laptopGa.costo)
print(laptopGa.realizarDiagnosticoSistema())
laptopB=laptopBusiness("MSI", "intel i7", 16,1000,24)
print(laptopB.realizarDiagnosticoSistema())