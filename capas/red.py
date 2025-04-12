def encapsular_red(datos_transporte):
    return {
        "cabecera_red": "IP",
        "datos": datos_transporte
    }

def desencapsular_red(mensaje):
    print(f"[Red] Cabecera recibida: {mensaje['cabecera_red']}")
    return mensaje["datos"]


def dividir_en_paquetes(bits, tiempos, tamano_paquete=100):
    paquetes = []
    for i in range(0, len(bits), tamano_paquete):
        paquete = {
            "id": i // tamano_paquete,
            "longitud": len(bits[i:i+tamano_paquete]),
            "datos": bits[i:i+tamano_paquete],
            "tiempos": tiempos[i:i+tamano_paquete]
        }
        paquetes.append(paquete)
    return paquetes

def reconstruir_bits(paquetes):
    # Ordenar por ID por si llegaron desordenados
    bits = []
    tiempos = []
    for paquete in paquetes:
        bits.extend(paquete["datos"])
        tiempos.extend(paquete["tiempos"])
    return {"binaria" : bits, "tiempo" : tiempos}
