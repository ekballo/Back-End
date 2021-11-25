#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

alt = float(input('Digite a altura [M/m]: '))
alt1 = float(input('Digite a altura [F/f]: '))

homens = alt * 72.7
mulheres = alt1 * 72.7

result = homens - 58
result1  = mulheres - 44.7

print('Peso ideal para Homens {}kg'.format(result))
print('Peso ideal para Mulheres {:.2f}kg'.format(result1))