import socket
import json
from capas.enlace import enviar_por_enlace, recibir_por_enlace

HOST = 'localhost'
PORT = 12345

def encapsular_transporte(datos_app):
    return {
        "cabecera_transporte": "TCP",
        "datos": datos_app
    }

def desencapsular_transporte(mensaje):
    print(f"[Transporte] Cabecera recibida: {mensaje['cabecera_transporte']}")
    return mensaje["datos"]


def enviar_paquetes(paquetes):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        for paquete in paquetes:
            enviar_por_enlace(s, paquete)

def recibir_paquetes():
    paquetes = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            while True:
                paquete = recibir_por_enlace(conn)
                if paquete is None:
                    break
                paquetes.append(paquete)
    return paquetes
