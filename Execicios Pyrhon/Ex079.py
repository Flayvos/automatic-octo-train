numlist = []
while True:
    n = int(input('Digite um numero: '))
    if n not in numlist:
        numlist.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    op = ' '
    while op not in 'NS':
        op = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if op[0] in 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(numlist)}')
