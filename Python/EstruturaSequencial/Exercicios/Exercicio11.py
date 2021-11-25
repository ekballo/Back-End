#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1 = float(input('Digite Primeiro Numero: '))
n2 = float(input('Digite Segundo Numero: '))
n3 = float(input('Digite Terceiro Numero: '))

a  = (n1 + n1 + n3) + (n2 / n2)
b  = (n1 ** n1) + n3
c  = n3 ** n3  

print('O dobro do primeiro com a metade do segundo é {}'.format(a))
print('A soma do triplo do primeiro com o terceiro é {:.2f}'.format(b))
print('O terceiro elevado ao Cubo é {:.2f}'.format(c))