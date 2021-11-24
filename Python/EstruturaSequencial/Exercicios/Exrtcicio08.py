#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.

valor = float(input('Digite o valor que ganha por hora: '))
horas = float(input('Digite quantas horas trabalhadas fez hoje: '))
dias = int(input('Quantos dias você trabalhou: '))

salário = valor * dias

salário = salário * horas

print('O valor ganho por horas é {:.2f}h'.format(valor))
print('A horas trabalhadas são {:.2f}h'.format(horas))
print('Quantos dias você trabalha no mês é {:.2f}'.format(dias))
print('A base salarial trabalhada no mês é {:.2f}'.format(salário,valor,horas))