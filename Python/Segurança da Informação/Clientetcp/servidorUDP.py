import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket Criado com Sucesso')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = 'Servidor: Olá seja bem vindo'

while 1:
    dados, endereço = s.recvfrom(4096)

if dados:
    print('Servidor enviado mensagem...')
    s.sendto(dados + (mensagem.ecode()), end)