from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
n = randint(0, 5)  # Faz o computador "PENSAR" em um numero.
print('-=-' * 20)
ni = int(input('Em que numero eu pensei?\n'))  # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if ni == n:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no numero {n} e nao no {ni}!')
