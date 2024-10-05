n = int(input('Digite um numero: '))
count2 = 0
for c in range(1, n + 1):
    if n % c != 0:
        print(f'\33[31m{c}', end=' ')
    elif n % c == 0:
        print(f'\33[33m{c}\33[m', end=' ')
        count2 += 1
print(f'\nO número {n} foi divisivel {count2} vezes')
if count2 == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO! ')
