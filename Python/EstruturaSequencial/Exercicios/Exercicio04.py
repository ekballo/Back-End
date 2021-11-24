#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

b1 = float(input('Digite a Nota do Primeiro bimestre: '))
b2 = float(input('Digite a Nota do Segundo bimestre: '))
b3 = float(input('Digite a Nota do Terceiro bimestre: '))
b4 = float(input('Digite a Nota do Quarto bimestre: '))

media = (b1+b2+b3+b4) / 4

print('A Média das notas bimestrais são {:.2f}'.format(media,b1,b2,b3,b4))