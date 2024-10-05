print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
posicao = 0
loop = 10
while loop != 0:
    posicao += 1
    loop -= 1
    an = primeiro + (posicao - 1) * razao
    print(an, end=' → ' if loop != 0 else ' → PAUSA\n')
    if loop == 0:
        loop = int(input('Quantos termos voce quer mostras a mais? '))
print(f'Progressao finalizada com {posicao} termos mostrados.')
