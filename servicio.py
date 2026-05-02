from abc import ABC, abstractmethod
from excepciones import ServicioError

class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, *args):
        pass


class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ServicioError("Horas inválidas")
        return self.costo_base * horas


class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        if dias <= 0:
            raise ServicioError("Días inválidos")
        return self.costo_base * dias


class Asesoria(Servicio):
    def calcular_costo(self, horas, descuento=0):
        if horas <= 0:
            raise ServicioError("Horas inválidas")
        total = self.costo_base * horas
        return total - (total * descuento)
