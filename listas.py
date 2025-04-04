# É um tipo mutável
# Suporta valores de qualquer tipo
# Tem vários métodos

# Criando lista:

lista1 = list()
lista2 = []
print(type(lista1), type(lista2))

# Exemplo lista com elementos:

listaE = [123, True, 'Joao Pedro', [7.77]]

print(listaE, '\n')

for i, e in enumerate(listaE):
    print(i, e)

# Da para alterar elementos da lista pelo indice

print(listaE[0])
listaE[0] = 1242352345
print(listaE[0])

# nomeDaLista.append(elemento) -> Adicionar elemento no final da lista

# nomeDaLista.insert(indice, elemento) -> Adicionar elemento no indice especificado. Move os elementos para frente

# nomeDaLista.pop(indice) -> Remover elemento do indice especificado, ou do final da lista sem indice especificado. 
#                            Pode atribuir a uma variavel para salvar o elemento removido

# nomeDaLista.del(indice) -> Remove um indice

# É possível somar duas listas listA + listaB atribuindo a uma nova variavel
# listaA.extend(listaB) -> irá modificar a propria listaA somando a listaB

# Cuidado com dados mutáveis

listaA = ['joao', 'pedro', 'paiva']
listaB = listaA

listaA[0] = 'Henrique'
print(listaB[0])

