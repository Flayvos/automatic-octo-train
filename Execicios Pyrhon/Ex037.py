n = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao: 
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
[ 0 ] Para ver todas as opcoes acima''')
o = int(input('Sua opcao: '))
if o == 1:
    print(f'{n} convertido para BINARIO e igual a {bin(n)[2:]}')
elif o == 2:
    print(f'{n} convertido para OCTAL e igual a {oct(n)[2:]}')
elif o == 3:
    print(f'{n} convertido para HEXADECIMAL e igual a{hex(n)[2:].upper()}')
elif o == 0:
    print(f'{n} em BINARIO : {bin(n)[2:]}')
    print(f'{n} em OCTAL : {oct(n)[2:]}')
    print(f'{n} em HEXADECIMAL : {hex(n)[2:].upper()}')
else:
    print('Opcao invalida. Tente novamente.')
