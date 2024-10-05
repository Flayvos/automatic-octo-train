from time import sleep
op = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while op != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa''')
    op = int(input('>>>>> Qual e a sua opcao ? '))
    if op == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} e {soma}')
    elif op == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} e {produto}')
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor e {maior}')
    elif op == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeir valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente')
    sleep(2)
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
