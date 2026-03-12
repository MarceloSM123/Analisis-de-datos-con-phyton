from laptop import laptop
import random

class laptopBusiness(laptop):
    def __init__(self, marca, procesador, memoria,almacenamiento,duracionBateria ,costo=500, impuestos=10):
        super().__init__(marca, procesador, memoria, costo, impuestos)
        self.almacenamiento=almacenamiento
        self.duracionBateria=duracionBateria
    def realizarDiagnosticoSistema(self):
        resultadoDiagnostico=super().realizarDiagnosticoSistema()
        resultadoBusiness=self.realizarDiagnosticoBusiness()
        resultadoDiagnostico["resultado Business"]=resultadoBusiness
        resultadoConexion=self.verificarConectividadRed()
        resultadoDiagnostico["conectividad"]=resultadoConexion
        return resultadoDiagnostico
    
    def realizarDiagnosticoBusiness(self):
        capacidad=[1000, 10000,100000]
        resultados={}
        for juego in capacidad:
            
            if self.almacenamiento>100000:
                fps="almacenamiento empresarial masivo"
            elif self.almacenamiento>10000:
                fps="almacenamiento empresarial"
            else:
                fps="almacenamiento basico"
            resultados[juego] = f"{fps} fps"
        return resultados
    def verificarConectividadRed(self):
        conectividad = {
            "wifi_disponible": random.choice([True, False]),
            "ethernet_disponible": random.choice([True, False]),
            "acceso_servidores_empresariales": random.choice([True, False]),
            "acceso_vpn": random.choice([True, False]),
            "latencia_red": random.choice(["Baja", "Media", "Alta"]),
            "velocidad_conexion": random.choice(["Rápida", "Moderada", "Lenta"]),
            "firewall_activo": random.choice([True, False]),
            "dns_resolviendo": random.choice([True, False])
        }
        
        if conectividad["wifi_disponible"] or conectividad["ethernet_disponible"]:
            if conectividad["acceso_servidores_empresariales"]:
                conectividad["estado_general"] = "Conectividad óptima"
            else:
                conectividad["estado_general"] = "Conectado sin acceso a servidores"
        else:
            conectividad["estado_general"] = "Sin conexión de red"
        
        if conectividad["latencia_red"] == "Baja":
            conectividad["recomendacion_red"] = "Adecuado para videoconferencias"
        elif conectividad["latencia_red"] == "Media":
            conectividad["recomendacion_red"] = "Posibles retrasos en comunicación"
        else:
            conectividad["recomendacion_red"] = "No recomendado para reuniones virtuales"
        
        return conectividad
    pass