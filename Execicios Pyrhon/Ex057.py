sexo = str(input('Informe seu sexo: [M/F] ')).strip().capitalize()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip().capitalize()
print(f'Sexo {sexo} registrado com sucesso.')
