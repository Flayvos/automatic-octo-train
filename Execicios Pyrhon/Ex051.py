print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
for c in range(1, 11):
    pa = termo + (c - 1) * razao
    print(pa, end =' → ')
print('ACABOU')
