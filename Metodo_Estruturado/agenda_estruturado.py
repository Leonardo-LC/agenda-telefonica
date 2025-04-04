agenda = {} #Criação do dicionário
nome = '' #Variável nome(input do usuário)
contato = '' #Variável número do contato(inputo do usuário)
while True:
    try: 
        a = int(input(
        'Digite 1 para Criar um contato ' \
        '\nDigite 2 para Listar os contato' \
        '\nDigite 3 para Editar um contato' \
        '\nDigite 4 para Remover um contato' \
        '\nDigite 5 para Sair\n'))
    except ValueError:
        a=0
    if a <= 0 or a > 5:
        print('Digite um valor válido de 1 a 5')
    if a == 1: #Funcionalidade criar contato
        nome = input('Digite o nome do contato:')
        contato = input('Digite o número de telefone do contato:')
        agenda[nome] = contato
        print('Contato criado com sucesso !')
        #print(agenda)#Deletar , verificação de criação de contato
    elif a == 2:
        print(agenda)
    elif a == 3:
        print('')
    elif a == 4:
        nome = input('Digite o nome do contato: ')
        print(f'Contato {nome} deletado com sucesso!')
    elif a==5: #Funcionalidade sair
       break