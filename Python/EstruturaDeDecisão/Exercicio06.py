#Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2:
    print('O primeiro numero é maior {}:'.format(n1))
elif n2 > n3:
    print('O segundo numero é maior {}'.format(n2))
else:
    print('O terceiro numero é maior {}'.format(n3))
print('Os numeros digitado entre o primeir {}, segundo {} e o terceiro o maior é {}'.format(n1,n2,n3,))
