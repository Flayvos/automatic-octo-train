valores = []
for cont in range(1,6):
    valores.append(int(input('Digite um valor: ')))
for c,v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
