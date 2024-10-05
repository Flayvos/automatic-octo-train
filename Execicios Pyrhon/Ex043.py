peso = float(input('Qual e seu peso? (Kg) '))
altura = float(input('Qual e sua altura? (m) '))
imc = peso/(altura**2)
print(f'O IMC dessa pessoa e de {imc:.1f}')
if imc < 18.5:
    print('Voce esta ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PARABENS, voce esta na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE!')
elif imc > 40:
    print('Voce esta em OBESIDADE MORBIDA, cuidado!')
