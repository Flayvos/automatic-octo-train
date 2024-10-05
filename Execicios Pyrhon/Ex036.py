vc = float(input('Valor da casa: R$'))
s = float(input('Salario do comprador: R$'))
f = int(input('Quantos anos de financiamento? '))
pm = vc / (f * 12)
s30 = s * 30 / 100
print(f'Para pagar uma casa de R${vc:.2f} em {f} anos a prestacao sera de R${pm:.2f}')
if pm <= s30:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
