from os import error
import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou !!!')
        print('Erro: {} '.format(e))
        sys.exit()
    print('Socket criado com sucesso !!')

    HostAlvo = input('Digite o host ou ip a ser conectado: ')
    PortaAlvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print('Cliente tcp conectado sucesso !!')
        s.shutdown(3)
    except socket.error as e:
        print('Não foi possivel conectar no Host')
        print('Erro: {}'.format(e))
        sys.exit()

if __name__ =="__main__":
    main()
