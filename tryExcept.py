nstr = input('Digite um numero: ')

try:
    nFloat = float(nstr)
    print('Float: ', nFloat)
    print(f'O dobro de {nstr} é {2*nFloat:.2f}.')
except:
    print('Isso não é um número')
