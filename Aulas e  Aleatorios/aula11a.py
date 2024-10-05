#print('\033[7;33;44mOla, mundo!\033[m')
"""a = 3
b = 5
print(f'Os valores sao \033[32m{a}\033[m e \033[31m{b}\033[m!!!')"""
nome = 'Flavio'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;97m'}
print('Ola prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'],nome,cores['limpa']))
