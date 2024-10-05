fim = n = count = tot = 0
while fim != 999:
    count += 1
    tot += n
    n = int(input('Digite um numero [999 para parar]: '))
    fim = n
print(f'Voce digitou {count-1} numeros e a soma entre eles foi {tot}.')
