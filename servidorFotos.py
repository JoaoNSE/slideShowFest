# coding=UTF-8
import array
import socket
import os
import io
import struct
import Image
import mostraImg
import clique_auto
import thread

thread.start_new_thread(mostraImg.mostraImg, ())
thread.start_new_thread(clique_auto.cliqueAuto, ())
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
contador = len(os.listdir('/home/joao/Documentos/projetoFinal/fotos'))
cont = 0

while True:
    print ("aceitando conexao")	
    con, cliente = tcp.accept()
    total = str()
    print ('Conectado por', cliente)
    path = "/home/joao/Documentos/projetoFinal/fotos/temp%s.jpeg"%str(contador)
    while True:
        
        msg = con.recv(9000000)
        total = total + msg
        
        s = bytearray(msg)
        cont += len(s)
        if not msg: break
        
    
    s = bytearray(total)
    print (cont)
    image = Image.open(io.BytesIO(s))
    image.LOAD_TRUNCATED_IMAGES = True
    image.save(path)
    contador += 1
    print ('Finalizando conexao do cliente', cliente)
    con.close() 
