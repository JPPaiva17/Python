# Coleção de conjuntos chave-valor

pessoa = {
    'nome':'João Pedro',
    'sobrenome':'Paiva',
    'idade': 21,
    'altura':180
}

pessoa['CorDosOlhos'] = 'Marrom'

print(pessoa.get('sobrenome'))

print(pessoa.get('pudim', None))