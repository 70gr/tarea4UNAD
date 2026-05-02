from excepciones import ReservaError
import datetime

def log_error(mensaje):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {mensaje}\n")

class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def procesar(self, *args):
        try:
            costo = self.servicio.calcular_costo(*args)
            self.estado = "Confirmada"
            return costo
        except Exception as e:
            log_error(str(e))
            raise ReservaError("Error en reserva") from e
