d = float(input('Qual o salario do funcionario? R$'))
a = d * 10/100 if d > 1250 else d * 15/100
print(f'Quem ganhava R${d:.2f} passa a ganhar R${a+d:.2f} agora.')
