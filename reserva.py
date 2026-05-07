from excepciones import ReservaError
import datetime

def log_error(mensaje):
    """
    Registra errores en el archivo logs.txt
    """
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - ERROR: {mensaje}\n")


class Reserva:
    """
    Clase que representa una reserva en el sistema
    """

    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def procesar(self, *args):
        """
        Procesa la reserva calculando el costo
        Maneja errores sin detener el sistema
        """
        try:
            costo = self.servicio.calcular_costo(*args)

        except Exception as e:
            log_error(str(e))
            raise ReservaError("Error al procesar la reserva") from e

        else:
            self.estado = "Confirmada"
            return costo

        finally:
            # Siempre se ejecuta
            print("Intento de procesamiento de reserva finalizado")

    def cancelar(self):
        """
        Cancela la reserva
        """
        if self.estado == "Confirmada":
            self.estado = "Cancelada"
        else:
            log_error("Intento de cancelar una reserva no confirmada")
            raise ReservaError("No se puede cancelar una reserva no confirmada")
