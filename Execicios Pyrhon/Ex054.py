from datetime import date
count18 = 0
count = 0
for c in range(1,8):
    ano = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    idade = date.today().year - ano
    if idade >= 18:
        count18 += 1
    else:
        count += 1
print(f'Ao todo tivemos {count18} pessoas maiores de idade')
print(f'E tambem tivemos {count} pessoas menores de idade')
