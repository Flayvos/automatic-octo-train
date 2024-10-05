lanche = ('Hamburguer','Suco','Pizza','Pudim','Batata Frita')

print(sorted(lanche))
# dado contido em determinada posicao
for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len (lanche)):
    print(f'Eu vou comer {lanche [cont]} na posicao {cont}')

for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
print('Comi pra caramba!')
