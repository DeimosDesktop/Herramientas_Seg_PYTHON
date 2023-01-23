from tkinter import Tk, Label, Button, StringVar,Entry, Frame, Text
import socket
root = Tk()
root.title("Aplicación Cliente")
root.minsize(400,200)
root.resizable(False, False)
frame_izq=Frame(root)
frame_inf=Frame(root)
frame_izq.grid(row=0,column=0,sticky="nsew")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

host = 'localhost'
port = 8050
obj = socket.socket()
obj.connect((host,port))
print("Conectado al servidor!")

def mandar(event):
    msg=mensaje.get()
    obj.send(msg.encode('ascii'))
    recibido = obj.recv(1024)
    print("Recibido")
    area_texto.configure(text="Mensaje Enviado: "+str(msg))
    mensaje.delete(0, "end")

frame_inf.grid(row=1,column=0,columnspan=4,sticky="ew",padx=5, pady=5)
area_texto=Label(frame_izq, padx=10, pady=10,bd=5, font=("Arial", 25))
area_texto.pack(expand=True, fill="both")
mensaje_label=Label(frame_inf,text="Escribe mensaje",bd=5, highlightthickness=2)
mensaje_label.pack(side="left",pady=10,padx=10)
mensaje=Entry(frame_inf,bd=5, highlightthickness=2, bg="gray")
mensaje.pack(side="left",ipadx=145,pady=10,padx=10, fill="both")
mensaje.bind("<Return>", mandar)
root.mainloop()