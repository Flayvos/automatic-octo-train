pessoas = list()
tabela = list()
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')).capitalize().strip())
    pessoas.append(float(input('Peso: ')))
    tabela.append(pessoas[:])
    pessoas.clear()
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
    if op[0] in 'N':
        break
for p in range(0, len(tabela)):
    if p == 0:
        maior = menor = tabela[p][1]
    if tabela[p][1] > maior:
        maior = tabela[p][1]
    if tabela[p][1] < menor:
        menor = tabela[p][1]
print('-=' * 30)
print(f'Voce cadastrou {len(tabela)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de', end=' ')
for x in range(0, len(tabela)):
    if tabela[x][1] == maior:
        print(f'{tabela[x][0]}', end=' ')
print(f'\nO menor peso foi de {menor}kg. Peso de', end=' ')
for y in range(0, len(tabela)):
    if tabela[y][1] == menor:
        print(f'{tabela[y][0]}', end=' ')
