n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print(f'Tirando {n1} e {n2}, a media do aluno e {media:.1f}')
if media < 5:
    print('O aluno esta REPROVADO.')
elif 5 <= media < 7:
    print('O aluno esta em RECUPERACAO.')
elif media >= 7:
    print('O aluno esta APROVADO.')
