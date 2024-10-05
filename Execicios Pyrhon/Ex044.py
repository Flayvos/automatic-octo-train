print('=' * 11, 'LOJAS TEIXEIRA', '=' * 11)
preco = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('Qual sua opcao? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    parcela = preco / 2
    total = preco
    print(f'Sua compra sera parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas > 2:
        total = preco + (preco * 20 / 100)
        print(f'Sua compra sera parcelada em {parcelas}x de R${total / parcelas:.2f} COM JUROS')
    else:
        total = preco
        print('OPCAO INVALIDA de pagamento. Tente novamente.')
else:
    total = preco
    print('OPCAO INVALIDA de pagamento. Tente novamente.')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
