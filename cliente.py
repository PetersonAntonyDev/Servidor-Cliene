

import socket
import requests
import json

client_host = '127.0.0.1'
client_port = 50000


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect( (client_host, client_port) )


print("conectado ao servidor")

while True:
    print("Digite 'fim' para encerrar sua conexão")
    cep = input("Digite o CEP sem os caracteres:")
    try:
        client.sendall(str.encode(cep))
        output = client.recv(1024)
        output = str(output, 'utf-8')
        dados = json.loads(output)
    except:
        print('ERRO')
        break
    if (cep == cep):
        print('Dados abaixo: ')
        print('Cep: {}'.format(dados['cep']))
        print('Logradouro: {}'.format(dados['logradouro']))
        print('Bairro: {}'.format(dados['bairro']))
        print('UF: {}'.format(dados['uf']))
        print('Localidade: {}'.format(dados['localidade']))
        print('DDD: {}'.format(dados['ddd']))
    elif (cep == 'fim'):
        break
    else:
        continue