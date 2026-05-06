from cliente import Cliente
def main():
    try:
        # Caso correcto
        c1 = Cliente("Juan", "juan@mail.com")
        print(c1.mostrar_info())
        # Caso incorrecto (nombre vacío)
        c2 = Cliente("", "correo@mail.com")
    except Exception as e:
        print("Error detectado:", e)

if _name_ == "_main_":
    main()
