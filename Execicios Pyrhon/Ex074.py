from random import randint

x = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Os valores sorteados foram: ', end='')
for cont in range(0, len(x)):
    print(f'{x[cont]}', end=' ')
print(f'\nO maior valor sorteado foi {max(x)}')
print(f'O menor valor sorteado foi {min(x)}')
