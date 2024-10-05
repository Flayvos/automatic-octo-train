tot = produto1000 = menor = 0
barato = ' '
print('-' * 34)
print('    LOJAS BARATÃO DO TEIXEIRA     ')
print('-' * 34)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    tot += preco
    if preco > 1000:
        produto1000 += 1
    if menor == 0 or menor > preco:
        menor = preco
        barato = produto
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op in 'N':
        break
print('{:-^34}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {produto1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato.strip()} que custa R${menor:.2f}')
