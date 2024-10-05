matrix = []
n = []
parsoma = coluna3 = maior2 = 0
for e in range(0, 3):
    for f in range(0, 3):
        n.append(int(input(f'Digite o valor para [{e},{f}]: ')))
    matrix.append(n[:])
    n.clear()
print('-=' * 30)
for t in range(0, 3):
    for j in range(0, 3):
        print(f'[{matrix[t][j]:^5}]', end='')
        if matrix[t][j] % 2 == 0:
            parsoma += matrix[t][j]
        if j == 2:
            coluna3 += matrix[t][j]
        if t == 1 and j == 0:
            maior2 = matrix[t][j]
        if t == 1:
            if matrix[t][j] > maior2:
                maior2 = matrix[t][j]
    print('\n', end='')
print('-=' * 30)
print(f'A soma dos valores pares é {parsoma}.')
print(f'A soma dos valores da terceira coluna é {coluna3}.')
print(f'O maior valor da segunda linha é {maior2}.')
