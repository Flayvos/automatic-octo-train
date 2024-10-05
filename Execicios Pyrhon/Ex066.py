qnt = total = n = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    qnt += 1
    total += n
print(f'A soma dos {qnt} valores foi {total}!')
