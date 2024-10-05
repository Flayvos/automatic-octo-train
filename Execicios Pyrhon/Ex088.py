from random import randint
from time import sleep

jogo = []
jogos = []
sor = 0
print('{:-^85}'.format('\n      JOGO DA MEGA SENA\n'))
qnt = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'SORTEANDO {qnt} JOGOS', '-=' * 3)
for z in range(0, qnt):
    while len(jogo) < 6:
        sor = randint(1, 60)
        if sor not in jogo:
            jogo.append(sor)
            jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
for a, b in enumerate(jogos):
    print(f'Jogo {a + 1}: {b}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
