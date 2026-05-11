import datetime
from cliente import Cliente
from excepciones import ClienteError, ServicioError, ErrorSistema
from servicio import ReservaSala, AlquilerEquipo, Asesoria

def registrar_log(mensaje):
    """Función que escribe los errores y eventos en el archivo logs.txt"""
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha_hora}] {mensaje}\n")

def main():
    registrar_log("--- INICIO DE PRUEBAS DEL SISTEMA DE GESTIÓN ---")
    print("Iniciando fase de validación e integración. Revisa logs.txt para el detalle de errores.")

    # ---------------------------------------------------------
    # BLOQUE 1: PRUEBAS DE CLIENTE (Casos 1 al 3)
    # ---------------------------------------------------------
    try:
        print("Prueba 1: Crear cliente válido...")
        c1 = Cliente("Juan Perez", "juan@mail.com")
        registrar_log(f"INFO: Prueba 1 Exitosa - {c1.mostrar_info()}")
    except Exception as e:
        registrar_log(f"ERROR INESPERADO Prueba 1: {e}")

    try:
        print("Prueba 2: Crear cliente con nombre vacío...")
        c2 = Cliente("", "correo@mail.com")
    except ClienteError as e:
        registrar_log(f"ERROR CONTROLADO Prueba 2 (ClienteError): {e}")

    try:
        print("Prueba 3: Crear cliente con correo inválido (sin arroba)...")
        c3 = Cliente("Ana", "ana_correo.com")
    except ClienteError as e:
        registrar_log(f"ERROR CONTROLADO Prueba 3 (ClienteError): {e}")

    # ---------------------------------------------------------
    # BLOQUE 2: PRUEBAS DE RESERVA DE SALA (Casos 4 al 6)
    # ---------------------------------------------------------
    try:
        print("Prueba 4: Calcular costo válido para Reserva de Sala...")
        s1 = ReservaSala("Sala VIP", 50000)
        costo = s1.calcular_costo(3) # 3 horas
        registrar_log(f"INFO: Prueba 4 Exitosa - {s1.descripcion()}, Costo total: ${costo}")
    except Exception as e:
        registrar_log(f"ERROR INESPERADO Prueba 4: {e}")

    try:
        print("Prueba 5: Calcular Reserva de Sala con horas negativas...")
        s2 = ReservaSala("Sala Ejecutiva", 50000)
        s2.calcular_costo(-2)
    except ServicioError as e:
        registrar_log(f"ERROR CONTROLADO Prueba 5 (ServicioError): {e}")

    try:
        print("Prueba 6: Calcular Reserva de Sala enviando texto en vez de números...")
        s3 = ReservaSala("Sala Juntas", 50000)
        s3.calcular_costo("cuatro")
    except ServicioError as e:
        registrar_log(f"ERROR CONTROLADO Prueba 6 (ServicioError): {e}")

    # ---------------------------------------------------------
    # BLOQUE 3: PRUEBAS DE ALQUILER DE EQUIPO (Casos 7 y 8)
    # ---------------------------------------------------------
    try:
        print("Prueba 7: Calcular costo válido para Alquiler de Equipo...")
        s4 = AlquilerEquipo("Video Beam 4K", 80000)
        costo = s4.calcular_costo(2) # 2 días
        registrar_log(f"INFO: Prueba 7 Exitosa - {s4.descripcion()}, Costo total: ${costo}")
    except Exception as e:
        registrar_log(f"ERROR INESPERADO Prueba 7: {e}")

    try:
        print("Prueba 8: Alquiler de Equipo con 0 días...")
        s5 = AlquilerEquipo("Portátil", 60000)
        s5.calcular_costo(0)
    except ServicioError as e:
        registrar_log(f"ERROR CONTROLADO Prueba 8 (ServicioError): {e}")

    # ---------------------------------------------------------
    # BLOQUE 4: PRUEBAS DE ASESORÍA (Casos 9 y 10)
    # ---------------------------------------------------------
    try:
        print("Prueba 9: Calcular Asesoría válida con 10% de descuento...")
        s6 = Asesoria("Asesoría Técnica", 100000)
        costo = s6.calcular_costo(4, descuento=0.1) # 4 horas, 10% descuento
        registrar_log(f"INFO: Prueba 9 Exitosa - {s6.descripcion()} calculada con descuento. Total: ${costo}")
    except Exception as e:
        registrar_log(f"ERROR INESPERADO Prueba 9: {e}")

    try:
        print("Prueba 10: Calcular Asesoría con descuento ilógico (150%)...")
        s7 = Asesoria("Asesoría Legal", 100000)
        s7.calcular_costo(2, descuento=1.5) # Descuento inválido
    except ServicioError as e:
        registrar_log(f"ERROR CONTROLADO Prueba 10 (ServicioError): {e}")

    registrar_log("--- FIN DE PRUEBAS DEL SISTEMA ---\n")
    print("Pruebas finalizadas con éxito. El sistema atrapó todas las excepciones sin detenerse.")

if __name__ == "__main__":
    main()