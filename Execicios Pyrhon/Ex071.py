print('{:=^80}'.format('\n          FTJ BANK\n'))
valor = int(input('Que valor você quer sacar ? R$'))
total = valor
valornota = 100
notas = 0
while True:
    if total >= valornota:
        total -= valornota
        notas += 1
    else:
        if notas > 0:
            print(f'Total de {notas} cedulas de R${valornota}')
        if valornota == 100:
            valornota = 50
        elif valornota == 50:
            valornota = 20
        elif valornota == 20:
            valornota = 10
        elif valornota == 10:
            valornota = 5
        elif valornota == 5:
            valornota = 1
        notas = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao FTJ BANK! Tenha um bom dia!')
