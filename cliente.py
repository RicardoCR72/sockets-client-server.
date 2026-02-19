import socket
import json
import time

def enviar_evento(tipo_evento, detalles):
    host = '127.0.0.1'
    puerto = 65432
    
    evento = {
        "tipo": tipo_evento,
        "detalles": detalles
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, puerto))
            s.sendall(json.dumps(evento).encode('utf-8'))
            
            data = s.recv(1024)
            respuesta = json.loads(data.decode('utf-8'))
            print(f"Respuesta del servidor para '{tipo_evento}': {respuesta['status']} - {respuesta['mensaje']}")
        except ConnectionRefusedError:
            print(f"Error: No se pudo conectar al servidor para enviar '{tipo_evento}'.")

if __name__ == "__main__":
    print("--- Iniciando envío de eventos ---")
    enviar_evento('orden', {"id_orden": 101, "item": "Laptop"})
    time.sleep(1)
    enviar_evento('ticket', {"id_ticket": 505, "asunto": "Falla de red"})
    time.sleep(1)
    enviar_evento('pago', {"monto": 1500.00, "metodo": "Tarjeta"})
    time.sleep(1)
    enviar_evento('desconocido', {"dato": "X"}) # Caso para forzar un NACK