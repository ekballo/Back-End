#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n1 = int(input('Digite o primeiro Numero: '))

if n1 < 0:
    print(' O nuemro é negativo {}'.format(n1))
else:
    print('O numero é positivo {}'.format(n1))