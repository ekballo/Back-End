#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
salário = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de finacioamento: '))

prestação = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {}'.format(casa,anos))
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONSEDIDO!')
else:
    print('Emprestimo NEGADO!')
