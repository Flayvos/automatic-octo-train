n = input('Digite um numero: ')
print('''Qual a base numerica do numero digitado?:
[ 0 ]BINARIO
[ 1 ]DECIMAL
[ 2 ]OCTAL
[ 3 ]HEXADECIMAL''')
o = int(input('Sua opcao: '))
if o == 0:
    d = int(n,2)
    print(f'{n} em DECIMAL: {d}')
    print(f'{n} em OCTAL: {oct(d)[2:]}')
    print(f'{n} em HEXADECIMAL: {hex(d)[2:].upper()}')
elif o == 1:
    d = int(n)
    print(f'{n} em BINARIO: {bin(d)[2:]}')
    print(f'{n} em OCTAL: {oct(d)[2:]}')
    print(f'{n} em HEXADECIMAL: {hex(d)[2:].upper()}')
elif o == 2:
    d = int(n,8)
    print(f'{n} em DECIMAL: {d}')
    print(f'{n} em BINARIO: {bin(d)[2:]}')
    print(f'{n} em HEXADECIMAL: {hex(d)[2:].upper()}')
elif o == 3:
    d = int(n,16)
    print(f'{n.upper()} em DECIMAL: {d}')
    print(f'{n.upper()} em BINARIO: {bin(d)[2:]}')
    print(f'{n.upper()} em OCTAL: {oct(d)[2:]}')
else:
    print('Opcao invalida. Tente novamente')
