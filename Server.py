import socket
import ipaddress
# FUNÇÕES DO SERVIDOR

def Calc_Raiz(lista):
    a = lista[0]
    b = lista[1]
    c = lista[2]
    delta = b**2.0 - 4.0*a*c
    print("delta "+ str(delta))
    if delta == 0:
        r = (-b/(2.0*a))
        return ["Existe 1 raiz real:", r]
    elif delta > 0:
        r1 = ((-b + delta**(1/2))/(2.0*a))
        r2 = ((-b - delta**(1/2))/(2.0*a))
        return ["Existem 2 raizes reais:", r1, r2]
    else:
        return ["Nao existem raizes reais."]

def IMC(lista):
    peso = lista[0]
    altura = lista[1]
    imc = peso/(altura**2)
    resul = ["Seu IMC:", imc]
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
    ip = ipv4
    resul = []
    classeA = ipaddress.IPv4Network(("10.0.0.0", "255.0.0.0"))  # or IPv4Network("10.0.0.0\8")
    classeB = ipaddress.IPv4Network(("172.16.0.0", "255.240.0.0"))  # or IPv4Network("172.16.0.0\12")
    classeC = ipaddress.IPv4Network(("192.168.0.0", "255.255.0.0"))  # or IPv4Network("192.168.0.0\16")

    ip = ipaddress.IPv4Address(ip)
    if ip is ipaddress.AddressValueError(ValueError):
        resul.append("Este IP é invalido\n")
        return resul
    else:
        resul.append("Este IP e valido\n")

    if ip in classeA:
        resul.append("Este IP esta na classe A\n")
    elif ip in classeB:
        resul.append("Este IP esta na classe B\n")
    elif ip in classeC:
        resul.append("Este IP esta na classe C\n")
    else:
        resul.append("Este IP esta IP esta na classe E ou D, que não possui uma divisao entre a network e o ID\n")

    if ip.is_loopback is True:
        resul.append("Este IP e um endereco de loopback\n")
    else:
        resul.append("Este IP nao e um endereco de loopback\n")

    hostname = socket.gethostname()
    ip_host = socket.gethostbyname(hostname)
    ip_host = ipaddress.IPv4Address(ip_host)

    if ip == ip_host:
        resul.append("O IP e local\n")
    else:
        resul.append("O IP nao e local\n")

    return resul

def fazArquivoResp(lista):
    with open("Respostas.txt", "w") as p:
        for valor in lista:
            p.write(str(valor)+" ")
    p.close()


# CONFIGURAÇÃO DO SERVIDOR
hostServer = ''
portServer = 8000

# Criando Socket
socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vinculando o socket ao servidor e a porta
socketObj.bind((hostServer, portServer))

# Aguardando uma conexão
socketObj.listen(5)
while True:
    # Aceitando conexão
    conexao, endereco = socketObj.accept()
    print("Servidor acessado por "+ str(endereco))
    while True:
        # Enviando o menu para o cliente
        with open("menuPrincipal.txt","r") as f:
            menu = f.read()
        f.close()
        conexao.send(menu.encode('utf-8'))
        # Recebendo resposta
        comando = conexao.recv(1024)
        comando = int(comando.decode())

        #Realizando operação do cliente
        if comando == 1:
            # Enviando novo menu
            with open("menuRaiz.txt", "r") as f:
                menu = f.read()
            f.close()
            conexao.send(menu.encode('utf-8'))
            # Recebendo nova resposta
            entradas = 3
            lista = []
            while (entradas > 0):
                valor = conexao.recv(1024)
                valor = int(valor.decode())
                lista.append(valor)
                entradas -= 1
            resul = Calc_Raiz(lista)
            fazArquivoResp(resul)
            with open("Respostas.txt", "r") as p:
                resp = p.read()
            p.close()
            conexao.send(resp.encode())

        elif comando == 2:
            # Enviando novo menu
            with open("menuIMC.txt", "r") as f:
                menu = f.read()
            f.close()
            conexao.send(menu.encode('utf-8'))
            # Recebendo nova resposta
            entradas = 2
            lista = []
            while (entradas > 0):
                valor = conexao.recv(1024)
                valor = float(valor.decode())
                lista.append(valor)
                entradas -= 1
            resul = IMC(lista)
            fazArquivoResp(resul)
            with open("Respostas.txt", "r") as p:
                resp = p.read()
            p.close()
            conexao.send(resp.encode())

        elif comando == 3:
            # Enviando novo menu
            with open("menuIPv4.txt", "r") as f:
                menu = f.read()
            f.close()
            conexao.send(menu.encode('utf-8'))
            # Recebendo nova resposta
            ipv4 = conexao.recv(1024)
            ipv4 = str(ipv4.decode())
            print(ipv4)
            resul = ClassificarIPV4(ipv4)
            fazArquivoResp(resul)
            with open("Respostas.txt", "r") as p:
                resp = p.read()
            p.close()
            conexao.send(resp.encode())

        elif comando == 4:
            while True:
                # Recebe mensagem
                message = conexao.recv(1024)
                if not message: break
                # Visualiza e Envia resposta
                print("Ele:" + message.decode('utf-8'))
                if message.decode() == "Tchau":
                    break
                message = input("Você:")
                conexao.send(message.encode('utf-8'))
        elif comando == 0:
            conexao.close()
            break
        else:
            message ="Essa função não existe em nosso Banco de Dados"
            conexao.send(message.encode())


