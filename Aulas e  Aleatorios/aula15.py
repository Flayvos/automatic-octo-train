n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
nome = 'Jose'
idade = 33
print(f'O {nome} tem {idade} anos.')    #PYTHOM 3.6+
print('O {} tem {} anos.'.format(nome,idade))   #PYTHON 3
print('O %s tem %d anos.' % (nome,idade))   #PYTHON 2
