import numpy as np
import matplotlib.pyplot as plt

def encapsular_aplicacion(paquete):
    return {
        "cabecera_aplicacion": "APPv1",
        "datos": {
            "id": paquete["id"],
            "longitud": paquete["longitud"],
            "datos": paquete["datos"],
            "tiempos": list(paquete["tiempos"])  # ✅ asegura serialización
        }
    }

def desencapsular_aplicacion(mensaje):
    print(f"[Aplicación] Cabecera recibida: {mensaje['cabecera_aplicacion']}")
    return mensaje["datos"]


def generar_senal(tipo='AC'):
    duracion = 0.2  # segundos
    fs = 1000
    tiempo = np.linspace(0, duracion, int(duracion * fs))

    if tipo == 'AC':
        frecuencia = 10  # Hz
        amplitud = 2.5 + (np.random.rand() * 0.6)
        valor_dc = 5.0 + (np.random.rand() * 0.6)
        senal = valor_dc + amplitud * np.sin(2 * np.pi * frecuencia * tiempo)
        descripcion = "AC (senoidal + DC)"
    else:
        valor_dc = 5.0
        senal = np.full_like(tiempo, valor_dc)
        descripcion = "DC (constante)"

    ruido = 0.8 * np.random.randn(len(tiempo))
    senal_con_ruido = senal + ruido

    ventana = 30
    senal_filtrada = np.convolve(senal_con_ruido, np.ones(ventana)/ventana, mode='same')

    umbral = valor_dc
    senal_binaria = (senal_filtrada > umbral).astype(int)

    return {
        "tiempo": tiempo.tolist(),
        "ideal": senal,
        "ruido": senal_con_ruido,
        "filtrada": senal_filtrada,
        "binaria": senal_binaria.tolist(),
        "umbral": umbral,
        "descripcion": descripcion
    }

def graficar_proceso(datos, nombreArchivo="senal.png", titulo="Señal Digital"):
    # Si los datos vienen como diccionario con tiempo, los usamos
    if isinstance(datos, dict): 
        if "tiempo" in datos:
            tiempo = datos["tiempo"]
            binaria = datos["binaria"]
            # print(f"[INFO] Tiempo de la señal: {tiempo} segundos")
        else:
            binaria = datos["binaria"]
            tiempo = np.linspace(0, len(binaria), len(binaria))
            print("perro")
        plt.figure(figsize=(12, 3))
        plt.step(tiempo, binaria, where="post")
        plt.title(titulo)
        plt.xlabel("Tiempo")
        plt.ylabel("Nivel de Señal")
        plt.grid(True)
        plt.ylim(-0.5, 1.5)
        plt.tight_layout()
        # plt.show()
        plt.savefig(nombreArchivo)
print("[✅] Gráfico guardado como salida_receptor.png")

