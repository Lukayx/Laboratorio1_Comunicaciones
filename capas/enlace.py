import json

def encapsular_enlace(datos_red):
    return {
        "cabecera_enlace": "ETH",
        "datos": datos_red
    }

def desencapsular_enlace(mensaje):
    print(f"[Enlace] Cabecera recibida: {mensaje['cabecera_enlace']}")
    return mensaje["datos"]

def enviar_por_enlace(socket, paquete):
    mensaje = json.dumps(paquete).encode('utf-8')
    # Enviar primero el tamaño
    largo = len(mensaje).to_bytes(4, 'big')  # 4 bytes para tamaño
    socket.sendall(largo + mensaje)

def recibir_por_enlace(socket):
    # Recibir el tamaño
    largo_bytes = socket.recv(4)
    if not largo_bytes:
        return None
    largo = int.from_bytes(largo_bytes, 'big')
    # Recibir el mensaje completo
    data = b''
    while len(data) < largo:
        chunk = socket.recv(largo - len(data))
        if not chunk:
            return None
        data += chunk
    return json.loads(data.decode('utf-8'))
