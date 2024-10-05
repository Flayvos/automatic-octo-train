count = 0
total = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        count += 1
        total += n
print(f'Voce informou {count} numeros PARES e a soma foi {total}')
