from random import shuffle

a = input('Primeiro aluno(a): ')
b = input('Segundo aluno(a): ')
c = input('Terceiro aluno(a): ')
d = input('Quarto aluno(a): ')
x = [a, b, c, d]
shuffle(x)
print(f'A ordem da apresentação será\n{x}')
