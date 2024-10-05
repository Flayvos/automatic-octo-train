from time import sleep

tabela = []
nomes = []
notas = []
alt = 0
while True:
    nome = str(input('Nome: ')).capitalize().strip()
    n1 = float(input('Nota1: '))
    n2 = float(input('Nota2: '))
    nomes.append(nome)
    notas.append(n1)
    notas.append(n2)
    nomes.append(notas[:])
    tabela.append(nomes[:])
    nomes.clear()
    notas.clear()
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()
    if op[0] == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-' * 26)
for n, alunos in enumerate(tabela):
    media = (alunos[1][0] + alunos[1][1]) / 2
    print(f'{n:<4} {alunos[0]:<10} {media:>8.1f}')
while True:
    print('-' * 35)
    alt = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if alt == 999 or alt > len(tabela):
        break
    else:
        print(f'Notas de {tabela[alt][0]} são {tabela[alt][1]}')
print('FINALIZANDO...')
sleep(1)
print('<<<', 'VOLTE SEMPRE', '>>>')
