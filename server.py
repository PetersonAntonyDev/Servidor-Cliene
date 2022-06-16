import socket
import requests

host = '127.0.0.1'
port = 50000 
print ("aguardando conexão...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind( (host, port) )
server.listen(10)
connection, addres = server.accept()

print(f'conectado em {addres}')
while True:
    
    cep = connection.recv(1024)
    print(cep)
    cep_srt = str(cep, 'utf-8') 
    #connection.sendall(bytearray(cep_srt[::-1], 'utf-8'))
    
    r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_srt))
    dados = r.text
    connection.sendall(bytearray(dados, 'utf-8'))
connection.close()