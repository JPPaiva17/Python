# Coleção de conjuntos chave-valor

pessoa = {
    'nome':'João Pedro',
    'sobrenome':'Paiva',
    'idade': 21,
    'altura':180
}

pessoa['CorDosOlhos'] = 'Marrom'

# Metodo Get

print(pessoa.get('sobrenome'))

print(pessoa.get('pudim', None))

# len(dicionario) -> qtd de chaves

print(len(pessoa))

# dicionario.keys() -> retorna as chaves do dicionario

print(list(pessoa.keys()))


# dicionario.values() -> retorna os valores do dicionario

print(list(pessoa.values()))


# dicionario.items() -> retorna o par chave-valor do dicionario

print(list(pessoa.items()))


# Shallow copy x Deep copy

pessoa2 = pessoa # -> atribuiu o mesmo lugar da memoria, modificou um modifica o outro

# Shallow copy -> mudou um nao altera o outro desde que sejam valores imutaveis, agora valores mutaveis ele continuara apontando
#                 para o mesmo lugar na memória

pessoa2 = pessoa.copy()

# Deep copy -> mudou um nao altera o outro
import copy

pessoa2 = copy.deepcopy(pessoa)

# Dicionario.pop('chave') -> exclui a chave e atribui a uma variavel 


# Dicionario.popitem() -> exclui a ultima chave e atribui a uma variavel 

# Dicionario.update({
#   'nome': 'Edinalvonerio Dariuspin'
#   'peso': 72934
# }) 
# 
# 
# -> Não apenas atualiza como adiciona novas chaves