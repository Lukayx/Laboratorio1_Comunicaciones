from capas.aplicacion import generar_senal, graficar_proceso, encapsular_aplicacion
from capas.red import dividir_en_paquetes, encapsular_red
from capas.transporte import enviar_paquetes, encapsular_transporte
from capas.enlace import encapsular_enlace

def main():
    tipo_senal = input("¿Qué tipo de señal deseas usar? (AC/DC): ").strip().upper()
    if tipo_senal not in ["AC", "DC"]:
        print("Tipo inválido. Usando AC por defecto.")
        tipo_senal = "AC"

    datos = generar_senal(tipo=tipo_senal)
    graficar_proceso(datos, "SeñalEnviada.png", "Señal Digital Enviada")

    paquetes = dividir_en_paquetes(datos["binaria"], datos["tiempo"])
    print(f"\n[INFO] Total de paquetes generados: {len(paquetes)}")
    print("[INFO] Enviando señal digital al receptor...\n")

    # Encapsulación por capas
    paquetes_encapsulados = []
    for paquete in paquetes:
        p = encapsular_aplicacion(paquete)
        p = encapsular_transporte(p)
        p = encapsular_red(p)
        p = encapsular_enlace(p)
        paquetes_encapsulados.append(p)

    enviar_paquetes(paquetes_encapsulados)
    print("[✅] Señal enviada correctamente.")

if __name__ == "__main__":
    main()
