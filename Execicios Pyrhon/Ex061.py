print('Gerador de PA')
print('-=' * 10)
count = 0
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
while count != 10:
    count += 1
    an = primeiro + (count - 1) * razao
    print(an, end=' → ')
print('FIM')
