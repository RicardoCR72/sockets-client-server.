import socket
import json

def iniciar_servidor():
    host = '127.0.0.1'
    puerto = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, puerto))
        s.listen()
        print(f"Servidor escuchando en {host}:{puerto}...")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"\nConectado a {addr}")
                data = conn.recv(1024)
                if not data:
                    break
                
                # Decodificar el evento recibido
                try:
                    evento = json.loads(data.decode('utf-8'))
                    tipo_evento = evento.get('tipo')
                    
                    print(f"Evento recibido: {tipo_evento}")
                    print(f"Detalles: {evento.get('detalles')}")
                    
                    # Generar respuesta (ACK / NACK)
                    if tipo_evento in ['orden', 'ticket', 'pago']:
                        respuesta = {"status": "ACK", "mensaje": f"Evento '{tipo_evento}' procesado exitosamente."}
                    else:
                        respuesta = {"status": "NACK", "mensaje": "Tipo de evento desconocido."}
                        
                    conn.sendall(json.dumps(respuesta).encode('utf-8'))
                except json.JSONDecodeError:
                    error = {"status": "NACK", "mensaje": "Formato de datos incorrecto."}
                    conn.sendall(json.dumps(error).encode('utf-8'))

if __name__ == "__main__":
    iniciar_servidor()