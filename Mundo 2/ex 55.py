maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa com menor peso tem {} kg e a pessoa com maior tem {} kg.'.format(menor, maior))