exp = list((str(input('Digite a expressão: '))))
valid = invalid = 0
for v in exp:
    if v in '(':
        valid += 1
    if v in ')':
        valid -= 1
    if valid < 0:
        invalid = 1
if invalid != 0 or valid != 0:
    print('invalido')
if invalid == 0 == valid:
    print('valido')
