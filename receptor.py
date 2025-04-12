from capas.transporte import recibir_paquetes, desencapsular_transporte
from capas.red import desencapsular_red, reconstruir_bits
from capas.aplicacion import graficar_proceso, desencapsular_aplicacion
from capas.enlace import desencapsular_enlace

def mostrar_y_desempaquetar(paquetes):
    print("Paquetes recibidos:")
    datos_puros = []
    for i, paquete in enumerate(paquetes):
        print(f"\n🔽 Paquete {i}:")
        p = desencapsular_enlace(paquete)
        p = desencapsular_red(p)
        p = desencapsular_transporte(p)
        mensaje = desencapsular_aplicacion(p)
        print(f"Bits recibidos: {mensaje}")
        datos_puros.append({
            "id": i,
            "datos": mensaje["datos"],
            "tiempos": mensaje["tiempos"]
        })
    return datos_puros

# Recibir datos
paquetes_encapsulados = recibir_paquetes()
paquetes = mostrar_y_desempaquetar(paquetes_encapsulados)

# Reconstruir señal
bits = reconstruir_bits(paquetes)

# Graficar
graficar_proceso(bits, "SeñalRecibida.png", "Señal Digital Recibida")