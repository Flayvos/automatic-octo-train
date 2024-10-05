a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if a == b == c:
        print('EQUILATERO!')
    elif a == b or b == c or c == a:
        print('ISOSCELES!')
    elif a != b != c:
        print('ESCALENO!')
else:
    print('Os segmentos acima NAO PODEM FORMAR um triangulo.')
