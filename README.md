# Client-Server Event Processing with Sockets 

## Description
This repository contains a basic Client-Server architecture implemented in **Python** using TCP sockets (`socket.SOCK_STREAM`). The system simulates an event-driven communication where a client sends specific events in JSON format, and the server processes them, returning an Acknowledgment (ACK) or Negative Acknowledgment (NACK).

### Supported Events:
* `orden` (Order)
* `ticket` (Support Ticket)
* `pago` (Payment)

## How to Run the Project 

To test the communication, you need to run the server and the client simultaneously in two separate terminal windows.

1. **Start the Server:**
   Open a terminal, navigate to the project directory, and run:
   ```bash
   python servidor.py
   Test ID,Test Case Description,Input Data,Expected Result,Actual Result,Status
TC01,"Send valid ""order"" event.","JSON with tipo: ""orden"" and product data.","Server responds with status: ""ACK"".",ACK - Evento 'orden' procesado exitosamente.,Passed ✅
TC02,"Send valid ""ticket"" event.","JSON with tipo: ""ticket"" and subject.","Server responds with status: ""ACK"".",ACK - Evento 'ticket' procesado exitosamente.,Passed ✅
TC03,"Send valid ""payment"" event.","JSON with tipo: ""pago"" and amount/method.","Server responds with status: ""ACK"".",ACK - Evento 'pago' procesado exitosamente.,Passed ✅
TC04,Send unregistered (invalid) event.,"JSON with tipo: ""desconocido"".","Server responds with status: ""NACK"".",NACK - Tipo de evento desconocido.,Passed ✅
TC05,Client attempts connection without active server.,Run client without server active.,Client throws connection error.,ConnectionResetError: [WinError 10054] / Connection error.,Passed ✅
