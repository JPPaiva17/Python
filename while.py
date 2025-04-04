# É um laço que repete até determinada condição for verdadeira

condicao = True

while condicao:
    nome = input('Qual é seu nome? ')
    print('Seu nome é ', nome)

    if nome == 'sair':
        break