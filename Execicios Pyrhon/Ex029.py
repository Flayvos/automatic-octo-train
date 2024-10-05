v = float(input('Qual a velocidade do carro? '))
if v > 80:
    m = (v - 80) * 7
    print(f'MULTADO! Voce excedeu o limite permitido que e de 80km/h\nVoce deve pagar uma multa de R${m:.2f}!')
print('Tenha um bom dia! Dirija com seguranca!')
