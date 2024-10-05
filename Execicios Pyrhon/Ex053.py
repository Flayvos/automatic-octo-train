frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
print(f'O inverso de {frase} é {frase[::-1]}')
if frase == frase[::-1]:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
