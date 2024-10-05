# Tabela de Classificacao da Serie A de 25/06/2021
times = (
    'Red Bull Bragantino', 'Athletico-PR', 'Fortaleza', 'Bahia', 'Palmeiras', 'Atletico-GO', 'Atletico-MG', 'Flamengo',
    'Fluminense', 'Santos', 'Corinthians', 'Ceara', 'Internacional', 'Juventude', 'Sport', 'Cuiaba', 'Sao Paulo',
    'Chapecoense', 'America-MG', 'Gremio')
print('-=' * 15)
print(f'Lista de times do Brasileirao: {times}')
print('-=' * 15)
print(f'Os 5 primeiros sao {times[:5]}')
print('-=' * 15)
print(f'Os 4 ultimos sao {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print('O Chapecoense esta na {}ª posicao'.format(times.index('Chapecoense')+1))
