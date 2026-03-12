#METODOS DE INSTANCIA
class laptop:
    def __init__(self, marca,procesador,memoria, costo=500, impuestos=10):
        self.marca=marca
        self.procesador=procesador
        self.memoria=memoria
        self.costo=costo
        self.impuestos=impuestos
    def valorFinal(self):
        return self.costo+self.impuestos
    def valorDescuento(self,descuento):
        return (self.costo*descuento)/100
    

laptopPepito=laptop("lenovo", "intel i7", "100gb", 1000, 120)
print(laptopPepito.__dict__)
print(laptopPepito.valorFinal())
print(laptopPepito.valorDescuento(10))