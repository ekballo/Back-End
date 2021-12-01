print('=*=' * 10)
print(''' Faça um Programa que leia três números e mostre o maior e o menor deles.''')
print('=*=' * 10)
a = int(input('Digite o primero Numero: '))
b = int(input('Digite o segundo Numero: '))
c = int(input('Digite o terceiro Numero: '))
#verificando que é menor
menor = a 
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Vertifcando quem é o maior
maior = a
if b > a and b < c:
    maior = b
if c > a and c < b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))