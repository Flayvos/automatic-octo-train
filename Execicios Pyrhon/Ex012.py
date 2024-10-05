p1 = float(input('Qual o preço do produto? R$'))
p2 = p1-(p1*5/100)
print(f'O produto que custava R${p1:.2f}, na promocao com desconto de 5% que e R${p1*5/100:.2f} vai custar R${p2:.2f}')
