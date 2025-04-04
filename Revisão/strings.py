# String e um tipo basico do python

palavra = "Paralelepipedo"
print(type(palavra))

# Strings podem ser somadas e multiplicadas

# Repetição
print(2*palavra)

# Concatenação
print(palavra + " e tijolo")

# Tambem podemos acessar certos caracteres da palavra atraves do index
# Index [inicio:fim(exclusivo):passo]
print(palavra[0])
print(palavra[0:2])
print(palavra[0::2])
print(palavra[-1::-1]) #Inverti a string comecei pelo indice -1(Ultimo caractere) com um passo de -1


# f-string

nome = 'Joao Pedro Paiva'
altura = 1.80
peso = 71
imc = peso / altura ** 2

frase = f'{nome} tem {altura} e pesa {peso}, portanto, seu IMC = {imc:.2f}'
print(frase)

# format

a = 'A'
b = 'B'
c = 1.13542352
formato = 'a = {}, b = {}, c = {:.2f}'.format(a, b, c)
print(formato)

# Alguns novos métodos

# frase.split(caracter) ->  transforma a string em uma lista de strings separando pelo caracter especificado dentro dos ()
#                           Se não tiver nada dentro dos () separará nas ' '

# frase.strip() -> tira os espaços em branco do inicio e do fim da string, lstrip e rstrip tambem existem 
