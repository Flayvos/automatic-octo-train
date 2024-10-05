from math import hypot
ops = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hip = hypot(ops, adj)
print(f'A hipotenusa vai medir {hip:.2f}')
