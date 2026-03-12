#SOBREESCRITURA DE METODos

from laptop import laptop
class laptopGaming (laptop):
    def __init__(self, marca,procesador,memoria,tarjetaGrafica, costo=500, impuestos=10):
        super().__init__(marca,procesador,memoria, costo, impuestos)
        self.tarjetaGrafica=tarjetaGrafica
    def realizarDiagnosticoSistema(self):
        resultadoDiagnostico= super().realizarDiagnosticoSistema() 
        resultadoJuegos=self.realizarDiagnosticoJuegos()
        resultadoDiagnostico["resultadoJuegos"]=resultadoJuegos   
        return resultadoDiagnostico
    def  realizarDiagnosticoJuegos(self):
        juegos=["fortnite", "COD","gta"]
        resultados={}
        for juego in juegos:
            fpsBase=30
            if "RTX" in self.tarjetaGrafica:
                fps=fpsBase*3
            elif "GTX" in self.tarjetaGrafica:
                fps=fpsBase*2
            else:
                fps=fpsBase
            resultados[juego] = f"{fps} fps"
        return resultados
    pass #importante