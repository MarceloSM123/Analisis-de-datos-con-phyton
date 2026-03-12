class auto:
    def __init__(self, marca, modelo, año, kilometraje=0):
     self.marca=marca
     self.modelo=modelo
     self.año=año
     self.kilometraje=kilometraje
    def mostrarInformacion(self):
       print(f"Marca: {self.marca} Modelo:{self.modelo} Año:{self.año} Kilometraje={self.kilometraje} ")
    def actualizarKilometraje(self,kilometrajeNuevo):
       if self.kilometraje<kilometrajeNuevo:
        self.kilometraje=kilometrajeNuevo
       else:
         print("No se puede reducir el kilometraje")
    def realizarViaje(self,kilometrosViaje):
      if kilometrosViaje<0:
        print("Ingrese valores positivos")
      else:
        self.kilometraje=self.kilometraje+kilometrosViaje
    def estadoAuto(self):
      if self.kilometraje<20000:
        print("Estoy como nuevo")
      elif self.kilometraje>=20000 and self.kilometraje<=100000:
        print("Ya estoy usado")
      elif self.kilometraje>100000:
        print("¡Ya déjame descansar por favor!")
    #METODO DE CLASE
    @classmethod
    def Toyota(cls):
      marca="Toyota"
      año=2026
      kilometraje=0
      modelo=""
      return cls(marca,modelo,año,kilometraje)
    #METODO ESTATICO
    @staticmethod
    def compKilometraje(auto1,auto2):
      if auto1.kilometraje==auto2.kilometraje:
        return "Tienen el mismo kilometraje"
      else:
        return "tienen distinto kilometraje"
    #METODO DE CLASE
    @classmethod
    def BMW(cls):
      marca="BMW"
      año=2026
      kilometraje=0
      modelo="Serie 3"
      return cls(marca,modelo,año,kilometraje)  
    #METODO ESTATICO
    @staticmethod
    def compMarca(auto1,auto2):
      if auto1.marca==auto2.marca:
        return "Tienen la misma marca"
      else:
        return "tienen distinta marca"  

autoFantastico=auto("tesla", "modElctrico", 2025,15000)

autoFantastico.mostrarInformacion()
autoFantastico.actualizarKilometraje(2000)
autoFantastico.realizarViaje(5000)
autoFantastico.estadoAuto()

Toyota1=auto.Toyota()
Toyota1.mostrarInformacion()
Toyota2=auto.Toyota()
Toyota2.mostrarInformacion()
print(auto.compKilometraje(Toyota1,Toyota2))

auto1=auto.Toyota()
auto2=auto.BMW()
print(auto.compMarca(auto1,auto2))