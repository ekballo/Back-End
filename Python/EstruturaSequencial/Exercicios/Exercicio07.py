#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

altura = float(input('Digite a altura do quadrado em metros: '))
largura = float(input('Digite a largura do quadrado em metros: '))

a = altura * largura

print ('O dobro da area é {:.1f}m2'.format(a))
