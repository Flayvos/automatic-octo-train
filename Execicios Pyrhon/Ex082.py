numlista = []
parlista = []
imparlista = []
while True:
    numlista.append(int(input('Digite um numero: ')))
    op = ' '
    while op[0] not in 'NS':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
    if op[0] in 'N':
        for n in numlista:
            if n % 2 == 0:
                parlista.append(n)
            if n % 2 == 1:
                imparlista.append(n)
        break
print('-=' * 30)
print(f'A lista completa e {numlista}')
print(f'A lista de pares e {parlista}')
print(f'A lista de impares e {imparlista}')
