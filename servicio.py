from abc import ABC, abstractmethod
from excepciones import ServicioError

class Servicio(ABC):
    """
    Clase abstracta que representa un servicio general.
    """

    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, *args):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):
    """
    Servicio de reserva de sala
    """

    def calcular_costo(self, horas):
        if not isinstance(horas, (int, float)):
            raise ServicioError("Las horas deben ser numéricas")
        if horas <= 0:
            raise ServicioError("Horas inválidas")
        return self.costo_base * horas

    def descripcion(self):
        return "Reserva de sala por horas"


class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos
    """

    def calcular_costo(self, dias):
        if not isinstance(dias, (int, float)):
            raise ServicioError("Los días deben ser numéricos")
        if dias <= 0:
            raise ServicioError("Días inválidos")
        return self.costo_base * dias

    def descripcion(self):
        return "Alquiler de equipos"


class Asesoria(Servicio):
    """
    Servicio de asesoría especializada
    """

    def calcular_costo(self, horas, descuento=0):
        if not isinstance(horas, (int, float)):
            raise ServicioError("Las horas deben ser numéricas")
        if horas <= 0:
            raise ServicioError("Horas inválidas")
        if descuento < 0 or descuento > 1:
            raise ServicioError("Descuento inválido")

        total = self.costo_base * horas
        return total - (total * descuento)

    def descripcion(self):
        return "Asesoría especializada"
