import socket
import os

# CONFIGURANDO CONEXÃO
serverHost = 'localhost'
serverPort = 8000

# Criando socket e conectando servidor
socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObj.connect((serverHost, serverPort))

# Comunicação com o servidor
while True:
    # Recebendo dados do servidor e enviando respostas
    serverMessage = socketObj.recv(1024)
    print(serverMessage.decode())
    comando = str(input())
    socketObj.send(comando.encode())
    comando = int(comando)
    if comando == 1:
        os.system('clear') or None
        # Novo Menu
        serverMessage = socketObj.recv(1024)
        print(serverMessage.decode())
        entradas = 3
        # Enviando dados
        while (entradas > 0):
            valor = str(input())
            socketObj.send(valor.encode())
            entradas -= 1
        # Recebendo resposta do Servidor
        resul = socketObj.recv(1024)
        print(resul.decode())

    elif comando == 2:
        # Novo Menu
        serverMessage = socketObj.recv(1024)
        print(serverMessage.decode())
        entradas = 2
        # Enviando dados
        while (entradas > 0):
            valor = str(input())
            socketObj.send(valor.encode())
            entradas -= 1
        # Recebendo resposta do Servidor
        resul = socketObj.recv(1024)
        print(resul.decode())

    elif comando == 3:
        # Novo Menu
        serverMessage = socketObj.recv(1024)
        print(serverMessage.decode())
        # Enviando dados
        ipv4 = str(input())
        socketObj.send(ipv4.encode())
        # Recebendo resposta do Servidor
        resul = socketObj.recv(1024)
        print(resul.decode())

    elif comando == 4:
        print("Chat do Servidor:")
        while True:
            message = input("Você:")
            socketObj.send(message.encode('utf-8'))
            if message == "Tchau":
                break
            message = socketObj.recv(1024)
            print("Ele:"+message.decode('utf-8'))

    elif comando == 0:
        socketObj.close()
        break

    else:
        message = socketObj.recv(1024)
        print(message.decode())
