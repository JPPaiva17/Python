palavraSecreta = input("Digite a Palavra secreta: ")
palavraMostrada = '_'*len(palavraSecreta)
tentativa = 0
ganhou = False
print("Palavra Formada: ", palavraMostrada)

while(not ganhou):
    tentativa +=1
    print("Tentativa Numero: ", tentativa)
    letra = input("Digite uma Letra: ")
    novaPalavraMostrada = ''

    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] == letra:
            novaPalavraMostrada += letra
        else:
            novaPalavraMostrada += palavraMostrada[i]
    
    palavraMostrada = novaPalavraMostrada
    print('Palavra Formada: ', palavraMostrada)

    if '_' not in palavraMostrada:
        ganhou = True


