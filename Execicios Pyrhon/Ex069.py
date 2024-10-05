count18 = countM = countF20 = 0
while True:
    print('-'*24)
    print('   CADASTRE UM PESSOA   ')
    print('-'*24)
    idade = int(input('Idade: '))
    if idade >= 18:
        count18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().capitalize()[0]
        if sexo in 'M':
            countM += 1
        elif sexo in 'F' and idade < 20:
            countF20 += 1
    print('-'*24)
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar ? [S/N] ')).strip().capitalize()[0]
    if op in 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {count18}')
print(f'Ao todo temos {countM} homens cadastrados')
print(f'E temos {countF20} mulheres com menos de 20 anos')
