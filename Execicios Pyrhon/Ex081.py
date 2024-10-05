numlista = []
while True:
    numlista.append(int(input('Digite um valor: ')))
    op = ' '
    while op[0] not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
    if op in 'N':
        break
print('-=' * 30)
print(f'Voce digitou {len(numlista)} elementos.')
numlista.sort(reverse=True)
print(f'Os valores em ordem decrecente sao {numlista}')
if 5 in numlista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao foi encontrado na lista!')
