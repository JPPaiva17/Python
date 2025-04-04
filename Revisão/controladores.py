#if / elif / else

frase1 = input("Você quer 'entrar' ou 'sair'? ")

if frase1 == 'entrar':
    print('Você entrou!')

elif frase1 == 'sair':
    print('Você saiu!')

else:
    print('Você digitou algo que não é válido!')

#-------------------------------------------------#
# Entrará em todas as condicoes e executara o print em todas

'''
n = 10

if(n > 2):
    print(n)
if(n > 4):
    print(n)
if(n > 6):
    print(n)
if(n > 8):
    print(n)
'''