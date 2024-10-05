n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
# Verificando o menor numero
x = n2
if n1 > n2 and n1 > n3:
    x = n1
if n3 > n2 and n3 > n1:
    x = n3
# Verificando o menor numero
y = n2
if n1 < n2 and n1 < n3:
    y = n1
if n3 < n2 and n3 < n1:
    y = n3
print(f'O menor valor digitado foi {y}')
print(f'O maior valor digitado foi {x}')
