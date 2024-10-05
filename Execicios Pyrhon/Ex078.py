lista = []
for n in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posicao {n}: ')))
print('=-' * 30)
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posicoes ', end='')
for pos, m in enumerate(lista):
    if m == max(lista):
        print(f'{pos}', end='... ')
print(f'\nO menor valor digitado foi {min(lista)} nas posicoes ', end='')
for pos, m in enumerate(lista):
    if m == min(lista):
        print(f'{pos}', end='... ')
