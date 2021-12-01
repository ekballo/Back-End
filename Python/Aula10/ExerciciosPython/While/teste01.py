resposta = 'sim'
while  resposta == 'sim':
    nivel = input('Digite o nivel de acesso: ').upper()
    if nivel == 'ADM' or nivel == 'USR':
        sexo = input('Digite seu sexo: ').upper
        if nivel == 'ADM':
            if sexo == 'Feminino':
                print('Olá Administradora')
            else:
                print('Olá Administrador')
        else:
            if sexo == 'Feminino':
                print('Olá usuaria')
            else:
                print('Olá usuario')
    elif nivel == 'GUEST':
        print('Olá visitante')
    else:
        print('Olá desconhecido(a)')
    resposta = input('Digite SIM para continuar: ').upper()