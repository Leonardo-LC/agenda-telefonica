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
        '\nDigite 5 para Pesquisar um contato' \
        '\nDigite 6 para Sair\n'))
    except ValueError:
        a=0

    if a <= 0 or a > 6: #Caso inválido
        print('Digite um valor válido de 1 a 6')
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
            while True:
                confirmarDeletar = input(f"o contato {nome} será deletado PERMANENTEMENTE. Deseja continuar? [s/n]: ").lower()
                if confirmarDeletar == 's':
                    del agenda[nome]
                    print(f'Contato {nome} deletado com sucesso!')
                    break
                elif confirmarDeletar == 'n':
                    print(f"O contato não foi deletado.")
                    break
                else:
                    print("É necessário digitar 's' para confirmar ou 'n' para cancelar a ação")

        else:
            print('Este contato não existe.')

    elif a == 5: #Funcionalidade de pesquisar contato
        nome = input("Digite o nome do contato: ").upper()
        if nome in agenda:
            print(f'Nome {nome}, Telefone: {agenda[nome]}')
        else:
            print("Contato não encontrado.")

    elif a == 6: #Funcionalidade sair
       break
    input("Pressione Enter para continuar...")
    print('\n\n\n\n\n\n\n\n')