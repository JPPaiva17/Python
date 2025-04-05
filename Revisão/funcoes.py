# toda função começa com def nomeDaFuncao(argumentos)

def soma(a = 0, b = 0):
    return a + b

print(soma())
print(soma(10))
print(soma(10, 20))

# *args

def soma2(*args):
    soma = 0
    for e in args:
        soma+=e
    return soma

print(soma2(1,2,3,4,5))


# Higher Order Functions -> funções que podem receber e/ou retornar outras funções
# First Class Functions -> Funções que são tratadas como outros tipos de dados comuns

# Closure

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falarBoaNoite = criar_saudacao('Boa noite')
falarBomDia = criar_saudacao('Bom dia')

print(falarBoaNoite('Joao'))
print(falarBomDia('Joao'))