somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):  # O Usuario coloca as informacoes.
    print('{:-^21}'.format(f' {p}º PESSOA '))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().capitalize()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    elif sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    elif sexo == 'F' and idade < 20:  # Contagem das mulheres com menos de 20 anos.
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A media de idade do grupo e de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos.')
