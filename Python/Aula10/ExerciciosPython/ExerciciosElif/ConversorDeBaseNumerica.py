#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal
num = int(input('Digite um numero inteiro: '))
print(''' Escolha uma das bases para conversão:
[ 1 ] Converter parta BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] coverter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igaul a {} '.format(num, bin(num)))
elif opção == 1:
    print('{} convertido para OCTAL é igaul a {} '.format(num, oct(num)))