cpf = input("Digite o CPF para validação: ")

cpf = ''.join([d for d in cpf if d.isdigit()])

if (len(cpf) == 11):
    
    #Verificação primeiro dígito
    soma = sum(int(cpf[i])*(10-i) for i in range(0,9))
    d1 = (soma*10)%11
    if d1 == 10:
        d1 = 0

    #verificação segundo dígito
    soma = sum(int(cpf[i])*(11-i) for i in range(0,10))
    d2 = (soma*10)%11
    if d2 == 10:
        d2 = 0

    verificador = f"{d1}{d2}"
    if(cpf[-2:] == verificador):
        print('Cpf verificado é válido!')
    else:
        print('Cpf verificado não é válido!')
