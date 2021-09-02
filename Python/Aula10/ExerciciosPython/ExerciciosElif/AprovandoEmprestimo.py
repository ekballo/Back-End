casa = float(input('Valor da Casa: R$'))
salario= float(input('Salario do Comprador: R$'))
anos = int(input('Qauntos ano de finacioamento?  '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2} em {} anos' .format(casa, anos), end='')
print('A prestação sera de R${:.2}' .format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO! s')
else:
    print('Emprestimo NEGADO! ')