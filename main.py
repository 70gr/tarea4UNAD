from cliente import Cliente
from servicio import ReservaSala
from reserva import Reserva

def main():
    try:
        cliente = Cliente("Juan", "juan@mail.com")
        servicio = ReservaSala("Sala VIP", 100)
        reserva = Reserva(cliente, servicio)

        print("Costo:", reserva.procesar(2))

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
