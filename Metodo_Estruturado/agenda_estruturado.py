agenda = {} #Criação do dicionário
nome = '' #Variável nome(input do usuário)
contato = '' #Variável número do contato(inputo do usuário)
while True:

    try: 
        a = int(input(
        'Bem vindo ao menu Central do programa Agenda'
        '\nDigite 1 para Criar um contato ' \
        '\nDigite 2 para Listar os contato' \
        '\nDigite 3 para Editar um contato' \
        '\nDigite 4 para Remover um contato' \
        '\nDigite 5 para Sair\n'))
    except ValueError:
        a=0

    if a <= 0 or a > 5: #Caso inválido
        print('Digite um valor válido de 1 a 5')
        continue

    elif a == 1: #Funcionalidade criar contato
        nome = input('Digite o nome do contato: ').upper()
        if nome in agenda:
            print('Este contato já existe.')
        else:
            contato = input('Digite o número de telefone do contato: ')
            agenda[nome] = contato
            print('Contato criado com sucesso !')

    elif a == 2: #Listar Contatos
        if agenda:
            for key in agenda:
                print(f'Nome : {key} , Telefone : {agenda[key]}')
        else:
            print('Agenda vazia! Crie novos contatos')
    elif a == 3: #Editar contato
        nome = input('Digite o nome do contato: ').upper()
        if nome in agenda:
            agenda[nome] = input('Digite o novo telefone do contato: ')
        else:
            print('Este contato não existe, operação não efetuada.')

    elif a == 4: #Deletar contato
        nome = input('Digite o nome do contato: ').upper()
        if nome in agenda:
            del agenda[nome]
            print(f'Contato {nome} deletado com sucesso!')
        else:
            print('Este contato não existe, operação não efetuada.')

    elif a==5: #Funcionalidade sair
       break
    input("Pressione Enter para continuar...")
    print('\n\n\n\n\n\n\n\n')