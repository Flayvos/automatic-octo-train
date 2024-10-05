produtos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('{:-^100}'.format('\n        LISTAGEM DE PREÇOS\n'))
for cont in range(0, len(produtos)):
    if cont % 2 == 0:
        print(f'{produtos[cont]:.<27}', end='')
    else:
        print(f'R${produtos[cont]:>7.2f}')
print('-'*36)
