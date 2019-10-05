from socket import socket, AF_INET, SOCK_STREAM
import os

# CONFIGURANDO CONEXÃO
HOST = 'localhost' #nome do host
PORT = 8000 #porta do servidor
ADDR = (HOST, PORT) #configurando endereço do servidor
BUFSIZ = 1024 #define tamanho do buffer das mensagens

# Criando socket e conectando servidor
socketObj = socket(AF_INET, SOCK_STREAM)
socketObj.connect(ADDR)

# Comunicação com o servidor
while True:
    # Recebendo dados do servidor e enviando respostas
    serverMessage = socketObj.recv(BUFSIZ)
    print(serverMessage.decode())
    comando = str(input())
    socketObj.send(comando.encode())
    comando = int(comando)
    if comando == 1:
        os.system('clear') or None
        # Novo Menu
        serverMessage = socketObj.recv(BUFSIZ)
        print(serverMessage.decode())
        entradas = 3
        # Enviando dados
        while (entradas > 0):
            valor = str(input())
            socketObj.send(valor.encode())
            entradas -= 1
        # Recebendo resposta do Servidor
        resul = socketObj.recv(BUFSIZ)
        print(resul.decode())

    elif comando == 2:
        # Novo Menu
        serverMessage = socketObj.recv(BUFSIZ)
        print(serverMessage.decode())
        entradas = 2
        # Enviando dados
        while (entradas > 0):
            valor = str(input())
            socketObj.send(valor.encode())
            entradas -= 1
        # Recebendo resposta do Servidor
        resul = socketObj.recv(BUFSIZ)
        print(resul.decode())

    elif comando == 3:
        # Novo Menu
        serverMessage = socketObj.recv(BUFSIZ)
        print(serverMessage.decode())
        # Enviando dados
        ipv4 = str(input())
        socketObj.send(ipv4.encode())
        # Recebendo resposta do Servidor
        resul = socketObj.recv(BUFSIZ)
        print(resul.decode())

    elif comando == 4:
        print("Chat do Servidor:")
        while True:
            message = input("Você:")
            socketObj.send(message.encode('utf-8'))
            if message == "Tchau":
                break
            message = socketObj.recv(BUFSIZ)
            print("Ele:"+message.decode('utf-8'))

    elif comando == 0:
        socketObj.close()
        break

    else:
        message = socketObj.recv(BUFSIZ)
        print(message.decode())
