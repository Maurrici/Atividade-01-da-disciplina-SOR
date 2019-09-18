import socket
#FUNÇÕES DO SERVIDOR
def Calc_Raiz(a,b,c):
    delta = b**2.0 - 4.0*a*c
    if delta == 0:
        r = (-b/(2.0*a))
        resul = [r]
        return resul
    elif delta > 0:
        r1 = ((-b + delta**(1/2))/(2.0*a))
        r2 = ((-b - delta**(1/2))/(2.0*a))
        resul = [r1, r2]
        return resul
    else:
        resul = [0]

def IMC(peso, altura):
    imc = peso/(altura**2)
    resul = [imc]
    if imc < 18.5:
        resul.append("Abaixo do peso")
        return resul
    elif imc >= 18.5 and imc <= 24.9:
        resul.append("Peso normal")
        return resul
    elif imc >= 25 and imc <= 29.9:
        resul.append("Sobrepeso")
        return resul
    elif imc >= 30 and imc <= 34.9:
        resul.append("Obesidade grau 1")
        return resul
    elif imc >= 35 and imc <= 39.9:
        resul.append("Obesidade grau 2")
        return resul
    elif imc >= 40:
        resul.append("Obesidade grau 3")
        return resul
    else:
        print("Erro no sistema")

def ClassificarIPV4(ipv4):


# CONFIGURAÇÃO DO SERVIDOR
hostServer = ''
portServer = 8000

# Criando Socket
socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Vinculando o socket ao servidor e a porta
socketObj.bind((hostServer, portServer))

#Aguardando uma conexão
socketObj.listen(5)
while True:
    #Aceitando conexão
    conexao, endereco = socketObj.accept()
    print("Servidor acessado por "+ str(endereco))
    while True:
        comando = conexao.recv(1024)
        int(comando.decode())
        if comando == 1:
            resul = Calc_Raiz()
        elif comando == 2:
            resul = IMC()
        elif comando == 3:
            resul = ClassificarIPV4()
        elif comando == 4:
            print("Chat do Servidor - Seja Bem Vindo:")
            #Recebe mensagem
            message = conexao.recv(1024)
            if not message: break
            #Visualiza e Envia resposta
            print("Ele:" + message.decode('utf-8'))
            message = input("Você:")
            conexao.send(message.encode('utf-8'))
        else:
            print("Essa função não existe em nosso Banco de Dados")


