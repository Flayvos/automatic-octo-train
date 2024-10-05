x = (int(input('Digite um numero: ')),
     int(input('Digite outro numero: ')),
     int(input('Digite mais um numero: ')),
     int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {x}')
print(f'O valor 9 apareceu {x.count(9)} vezes')
if 3 in x:
    print(f'O valor 3 apareceu na {x.index(3) + 1}ª posicao')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print('Os valores pares digitados foram ', end='')
for cont in range(0, len(x)):
    if x[cont] % 2 == 0:
        print(x[cont], end=' ')
