#teste de commit

cpf = input('Digite seu CPF: ')

cpf_fixed = cpf.replace('.', '').replace('-','')

def digito1(cpf_fixed):

    lista_valroes = []
    indice_inicial = 0
    indice_inicial_multiplicador = 10

    for x in range(9):
        valor_atual = cpf_fixed[indice_inicial]
        resposta = int(valor_atual) * indice_inicial_multiplicador
        lista_valroes.append(resposta)
        indice_inicial += 1
        indice_inicial_multiplicador -= 1
    
    soma = 0
    for i in lista_valroes:
        soma += i
    
    if (soma % 11) < 2:
        digito = 0
    elif (soma % 11) >= 2:
        digito = 11 - (soma % 11)
    return digito

def digito2(cpf_fixed):
    lista_valroes = []
    indice_inicial = 0
    indice_inicial_multiplicador = 11

    for x in range(10):
        valor_atual = cpf_fixed[indice_inicial]
        resposta = int(valor_atual) * indice_inicial_multiplicador
        lista_valroes.append(resposta)
        indice_inicial += 1
        indice_inicial_multiplicador -= 1
    
    soma = 0
    for i in lista_valroes:
        soma += i
    
    if (soma % 11) < 2:
        digito = 0
    elif (soma % 11) >= 2:
        digito = 11 - (soma % 11)
    return digito

if digito1(cpf_fixed) == int(cpf_fixed[9]) and digito2(cpf_fixed) == int(cpf_fixed[10]):
    print(f'CPF: {cpf} Válido!')
else:
    print(f'O CPF {cpf} é inválido!')