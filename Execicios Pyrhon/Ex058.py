from random import randint

cpu = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Sera que voce consegue advinhar qual foi?')
count = 0
n = -1
while n != cpu:
    count += 1
    n = int(input('Qual é seu palpite? '))
    if n > cpu:
        print('Menos... Tente mais uma vez.')
    elif n < cpu:
        print('Mais... Tente mais uma vez.')
print(f'Acertou com {count} tentativas. Parabéns!')
