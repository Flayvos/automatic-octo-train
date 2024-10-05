pesos = []
for c in range(1, 6):
    peso = float(input(f'Peso da {c}º pessoa: '))
    pesos += [peso]
print(f'O maior peso lido foi de {max(pesos):.1f}Kg')
print(f'O menor peso lido foi de {min(pesos):.1f}Kg')
