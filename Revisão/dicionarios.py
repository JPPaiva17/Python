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