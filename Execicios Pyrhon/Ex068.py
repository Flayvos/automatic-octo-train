from random import randint
count = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    print('=-' * 15)
    cpu = randint(0, 10)
    n = int(input('Diga um valor: '))
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('Par ou Ímpar? [P/I]: ')).strip().capitalize()[0]
    tot = cpu + n
    if tot % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print('-' * 30)
    print(f'Você jogou {n} e o computador jogou {cpu}. Total de {tot} DEU {resultado}')
    print('-' * 30)
    if jogador == resultado[0]:
        print('Você VENCEU!\nVamos jogar novamente...')
        count += 1
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {count}', 'vezes.' if count != 1 else 'vez.')
