qnt = numaior = numenor = numtot = num = 0
resposta = ''
while resposta != 'N':
    num = int(input('Digite um numero: '))
    numtot += num
    qnt += 1
    if qnt == 1:
        numaior = numenor = num
    else:
        if num > numaior:
            numaior = num
        elif num < numenor:
            numenor = num
    resposta = str(input('Quer continuar [S/N]: ')).strip().capitalize()[0]
media = numtot / qnt
print(f'Voce digitou {qnt} numeros e a media foi {media}')
print(f'O maior valor foi {numaior} e o menor foi {numenor}')
