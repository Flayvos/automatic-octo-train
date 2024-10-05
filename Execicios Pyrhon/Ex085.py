num = [[], []]
for x in range(1, 8):
    z = int(input(f'Digite o {x}o. Valor: '))
    if z % 2 == 0:
        num[0].append(z)
    else:
        num[1].append(z)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(num[0])}')
print(f'Os valores impares digitados foram: {sorted(num[1])}')
