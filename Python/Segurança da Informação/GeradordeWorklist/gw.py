import itertools

string = input('Digite uma frase: ')

resultado = itertools.permutations(string,len(string))

for i in resultado:
    print(''.join(i))

