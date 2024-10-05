n = str(input('Qual e seu nome? '))
if n == 'Flavio':
    print('Que nome bonito!')
elif n == 'Pedro' or n == 'Maria' or n == 'Paulo':
    print('Seu nome e bem popular no Brasil.')
elif n in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome e bem normal.')
print(f'Tenha um bom dia, {n}!')
