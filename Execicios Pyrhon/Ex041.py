from datetime import date
nasc = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'O atleta tem {idade} anos.')
if idade < 10:
    print(f'Classificacao: MIRIM')
elif idade < 15:
    print(f'Classificacao: INFANTIL')
elif idade < 20:
    print(f'Classificacao: JUNIOR')
elif idade < 24:
    print(f'Classificacao: SENIOR')
else:
    print(f'Classificacao: MASTER')
