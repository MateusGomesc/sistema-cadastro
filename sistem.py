from os import system
import emoji

def menu():
    print('-'*24)
    print('          MENU')
    print('-'*24)
    print('[1] - Cadastrar')
    print('[2] - Mostar cadastrados')
    print('[0] - Encerrar')
    print('-'*24)

def leiaopc(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            system('cls')
            menu()
            print(emoji.emojize('\033[31mDIGITO INVALIDO, digite novamente.:x:\033[m', language='alias'))
            continue
        else:
            if num < 0 or num > 2:
                system('cls')
                menu()
                print(emoji.emojize('\033[31mNUMERO INVALIDO, digite novamente.:x:\033[m', language='alias'))
                continue
            else:
                return num

def cabeçalho(msg):
    print('-'*(len(msg) + 4))
    print(f'  {msg}')
    print('-'*(len(msg) + 4))
    print('\n')

def leiaidade(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            system('cls')
            cabeçalho('CADASTRO')
            print(emoji.emojize('\033[31mDIGITO INVALIDO, digite novamente.:x:\033[m', language='alias'))
            continue
        else:
            return num

def leianome(msg):
    while True:
        try:
            nome = str(input(msg)).strip()
        except:
            system('cls')
            cabeçalho('CADASTRO')
            print(emoji.emojize('\033[31mNOME INVALIDO, digite novamente.:x:\033[m', languagem='alias'))
            continue
        else:
            if nome.isalpha() == False or nome == '':
                system('cls')
                cabeçalho('CADASTRO')
                print(emoji.emojize('\033[31mNOME INVALIDO, digite novamente.:x:\033[m', language='alias'))
                continue
            else:
                return nome

def tabela(lista):
    system('cls')
    print('-'*20)
    print('     CADASTRADOS')
    print('-'*20)
    print('NOME           IDADE')
    print('-'*20)
    for i in range(0, len(lista)):
        print(f'{lista[i]["nome"]:<10} {lista[i]["idade"]:^10}')