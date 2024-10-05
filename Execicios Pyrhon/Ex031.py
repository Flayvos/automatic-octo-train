d = float(input('Qual e a distancia da viagem? '))
print(f'Voce esta prestes a comecar uma viagem de {d}Km.')
p = d * 0.45 if d > 200 else d * 0.50
print(f'E o preco da sua passagem sera de R${p:.2f}')
