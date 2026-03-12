class auto:
    def __init__(self, marca, modelo, año, kilometraje=0):
     self.marca=marca
     self.modelo=modelo
     self.año=año
     self.kilometraje=kilometraje
    def mostrarInformacion(self):
       print(f"Marca: {self.marca} Modelo:{self.modelo} Año:{self.año} ")
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
autoFantastico=auto("tesla", "modElctrico", 2025,15000)

autoFantastico.mostrarInformacion()
autoFantastico.actualizarKilometraje(2000)
autoFantastico.realizarViaje(5000)
autoFantastico.estadoAuto()