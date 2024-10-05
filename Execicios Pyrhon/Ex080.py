numlista = []
for n in range(0, 5):
    valor = int(input('Digite um valor: '))
    if n == 0 or valor >= max(numlista):
        numlista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numlista):
            if valor <= numlista[pos]:
                numlista.insert(pos, valor)
                print(f'Adicionado na posicao {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {numlista}')
