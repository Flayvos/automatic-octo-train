from datetime import date
a = int(input('Que ano quer analisar? Coloque 0 para analizar o ano atual: '))
if a == 0:
    a = date.today().year
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(f'O ano {a} e E BISSEXTO!')
else:
    print(f'O ano {a} NAO e BISSEXTO!')
