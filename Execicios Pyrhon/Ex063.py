print('{:-^84}'.format('\nSequencia de Fibonacci\n'))
loop = int(input('Quantos termos voce quer mostrar? '))
f1 = 0
f2 = 1
print('~' * 30)
while loop != 0:
    loop -= 1
    print(f1, end=' → ')
    f1 += f2
    f2 = f1 - f2
print('FIM')
print('~' * 30)
