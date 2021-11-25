#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

alt = float(input('Digite sua altura seperada por ponto (Ex 1.69) : '))
vt = 72.7 * alt
resultado = vt - 58
print('Seu peso idela seria {:.2f}kg'.format(resultado))