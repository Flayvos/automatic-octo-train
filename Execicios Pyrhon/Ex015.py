d = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
v = d * 60 + km * 0.15
print(f'O valor total do aluguel ficou por R${v:.2f}')
