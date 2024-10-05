matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for e in range(0, 3):
    for x in range(0, 3):
        matrix[e][x] = int(input(f'Digite um valor para [{e},{x}]: '))
print('-=' * 30)
for y in range(0, len(matrix)):
    for z in range(0, len(matrix)):
        print(f'[{matrix[y][z]:^5}]', end='')
    print()
