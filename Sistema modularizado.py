from os import system
import sistem
import pickle
from time import sleep
import emoji

cadastros = {}
lista = []
opc = 1

while opc != 0:
    # Recebe opção do ususario
    system('cls')
    sistem.menu()
    opc = sistem.leiaopc('Digite sua opção: ')

    # Area de cadastro
    if opc == 1:
        # Recebe nome
        system('cls')
        sistem.cabeçalho('CADASTRO')
        cadastros['nome'] = sistem.leianome('Nome: ')

        # Recebe idade
        system('cls')
        sistem.cabeçalho('CADASTRO')
        cadastros['idade'] = sistem.leiaidade('Idade: ')

        # Inseri na lista e limpa dicionario
        lista.append(cadastros.copy())
        cadastros.clear()

        # Salvando lista
        try:
            with open('lista.pkl', 'wb') as arquivo:
                pickle.dump(lista, arquivo)
        except:
            system('cls')
            sistem.cabeçalho('CADASTRO')
            print(emoji.emojize('\033[mERRO ao fazer o cadastro.:x:\033[m', language='alias'))
            print('Aguarde o programa reiniciar...')
            sleep(3)
            continue
        else:
            system('cls')
            sistem.cabeçalho('CADASTRO')
            print(emoji.emojize('\033[32mCADASTRO EFETUADO COM SUCESSO!:white_check_mark:\033[m', language='alias'))
            sleep(3)
            continue
    elif opc == 2:
        system('cls')
        sistem.cabeçalho('CADASTRADOS')
        
        # Carrega a lista
        try:
            with open('lista.pkl', 'rb') as arquivo:
                lista = pickle.load(arquivo)
        except:
            system('cls')
            sistem.cabeçalho('CADASTRADOS')
            print(emoji.emojize('\033[31mERRO ao carregar a lista.:x:\033[m', language = 'alias'))
            sleep(3)
            continue
        else:
            # Mostra lista
            sistem.tabela(lista)
            evento = ' '
            while evento != '':
                evento = input('\nENTER para voltar ao menu.')
                if evento != '':
                    print(emoji.emojize('\033[31mDigite invalido!:x: Digite novamente.\033[m', language='alias'))
                    continue
            continue
print(emoji.emojize('<<< FINALIZANDO:wave: >>>', language = 'alias'))
sleep(3)