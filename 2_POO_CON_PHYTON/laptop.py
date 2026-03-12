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
   #METODOS ESTATICOS EN LA CLASE
    @staticmethod
    def compararCosto(Laptop1,Laptop2):
        if Laptop1.costo==Laptop2.costo:
            return "Los costos son iguales"
        else:
            return "los costos son diferentes"
    #METODO DE CLASE
    @classmethod
    def    asusLaptop(cls,costo):
        marca="asus"
        procesador="i5" 
        memoria=16
        return cls(marca,procesador,memoria,costo)

