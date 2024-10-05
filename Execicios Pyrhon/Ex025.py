n = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in n.title().split()))
