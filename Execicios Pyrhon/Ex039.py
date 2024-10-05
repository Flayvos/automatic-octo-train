from datetime import date

a = int(input('Ano de nascimento: '))  # ano de nascimento do usuario
ia = date.today().year - a  # idade atual do usuario
print(f'Quem nasceu em {a} tem {ia} anos em {date.today().year}.')
if ia < 18:
    print(f'Ainda faltam {18 - ia} anos para o alistamento')
    print(f'Seu alistamento sera em {(18 - ia) + date.today().year}.')
elif ia > 18:
    print(f'Voce ja deveria ter se alistado ha {ia - 18} anos.')
    print(f'Seu alistamento foi em {date.today().year - (ia - 18)}.')
else:
    print('Voce tem que se alistar IMEDIATAMENTE!')
