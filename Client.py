import socket
#CONFIGURANDO CONEXÃO
serverHost = 'localhost'
serverPort = 8000

#Criando socket e conectando servidor
socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObj.connect((serverHost, serverPort))


