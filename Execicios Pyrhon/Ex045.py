from time import sleep
from random import randint

print('''Suas opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
op = int(input('Qual e a sua jogada? '))
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
if op > 2:
    print('OPCAO INVALIDA.Tente novamente.')
elif 0 <= op <= 2:
    if (op == 0 and cpu == 2) or (op == 1 and cpu == 0) or (op == 2 and cpu == 1):
        resultado = 'JOGADOR VENCE'
    elif op == cpu:
        resultado = 'EMPATE'
    else:
        resultado = 'COMPUTADOR VENCE'
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=' * 11)
    print(f'Jogador jogou {itens[op]}')
    print(f'Computador jogou {itens[cpu]}')
    print('-=' * 11)
    print(f'{resultado}')
