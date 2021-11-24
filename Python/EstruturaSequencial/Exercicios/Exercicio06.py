#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input('Digite o valor do círculo em m2: '))

pi = 3.14

area = pi * (raio ** 2)
print('A area do círculo é de {:.1f}'.format(area,pi))