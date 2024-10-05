# Imports
from time import sleep

print('\033[1;36m=-=\033[1;30m' * 25)
print('\033[1;36m=-=' * 7, '\033[1;35mJogo da Velha\033[1;30m | by:Lucas Inacio', '\033[1;36m=-=\033[1;30m' * 7)

# Loop While
sentinel = 0
while sentinel == 0:
    print('\033[1;36m=-=\033[1;30m' * 25)
    modo = input('Escolha o modo de jogo:\nOu digite <sair>\n\n[ 1 ] - Dois jog'
                 'adores\n[ 2 ] - Contra bot\n\n>>>').strip().lower()

    # Modo: Dois jogadores
    if modo == '1':
        print('\033[1;36m=-=\033[1;30m' * 25)
        jogr1 = str(input('Nome do primeiro jogador [ X ]:\n>>>')).strip().capitalize()
        jogr2 = str(input('Nome do segundo jogador [ O ]:\n>>>')).strip().capitalize()
        print('\033[1;36m=-=\033[1;30m' * 25)
        q1 = '1'
        q2 = '2'
        q3 = '3'
        q4 = '4'
        q5 = '5'
        q6 = '6'
        q7 = '7'
        q8 = '8'
        q9 = '9'
        vitjogr1 = 0
        vitjogr2 = 0
        vitvelha = 0
        rodada = 0
        vez = 1
        vezL = ''
        veznome = ''
        while rodada == 0:
            if vez == 1:
                vez = 2
                vezL = '\033[1;31mX\033[1;30m'
                veznome = jogr1
            elif vez == 2:
                vez = 1
                vezL = '\033[1;31mO\033[1;30m'
                veznome = jogr2
            print("""Escolha um número de 1 a 9 de\nacordo com o lugar desejado.\n\n
                            |     |
                         {}  |  {}  |  {}
                       -----+-----+-----
                         {}  |  {}  |  {}
                       -----+-----+-----
                         {}  |  {}  |  {}
                            |     |""".format(q1, q2, q3, q4, q5,
                                              q6, q7, q8, q9))
            print('\n\nPlacar:\n\033[1;31m{}\033[1;30m ='
                  ' {}\n\033[1;31m{}\033[1;30m = {}\n\033[1;31mVelha\033[1;30m = {}'.format(jogr1, vitjogr1, jogr2,
                                                                                            vitjogr2, vitvelha))
            jogada = input('\n\033[1;31m{}\033[1;30m sua vez:\nOu digite <voltar>\n>>>'.format(veznome)).strip().lower()
            if jogada == '1' and q1 == '1':
                q1 = vezL
            elif jogada == '2' and q2 == '2':
                q2 = vezL
            elif jogada == '3' and q3 == '3':
                q3 = vezL
            elif jogada == '4' and q4 == '4':
                q4 = vezL
            elif jogada == '5' and q5 == '5':
                q5 = vezL
            elif jogada == '6' and q6 == '6':
                q6 = vezL
            elif jogada == '7' and q7 == '7':
                q7 = vezL
            elif jogada == '8' and q8 == '8':
                q8 = vezL
            elif jogada == '9' and q9 == '9':
                q9 = vezL
            elif jogada == 'voltar':
                break
            else:
                print('Opcão inválida, perdeu a vez \033[1;31m{}\033[1;30m.'.format(veznome))
                sleep(4)
            if q1 == '\033[1;31mX\033[1;30m' and q2 == '\033[1;31mX\033[1;30m' and q3 == '\033[1;31mX\033[1;30m':
                vitjogr1 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr1))
                sleep(4)
            elif q4 == '\033[1;31mX\033[1;30m' and q5 == '\033[1;31mX\033[1;30m' and q6 == '\033[1;31mX\033[1;30m':
                vitjogr1 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr1))
                sleep(4)
            elif q7 == '\033[1;31mX\033[1;30m' and q8 == '\033[1;31mX\033[1;30m' and q9 == '\033[1;31mX\033[1;30m':
                vitjogr1 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr1))
                sleep(4)

            elif q1 == '\033[1;31mX\033[1;30m' and q4 == '\033[1;31mX\033[1;30m' and q7 == '\033[1;31mX\033[1;30m':
                vitjogr1 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr1))
                sleep(4)
            elif q2 == '\033[1;31mX\033[1;30m' and q5 == '\033[1;31mX\033[1;30m' and q8 == '\033[1;31mX\033[1;30m':
                vitjogr1 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr1))
                sleep(4)
            elif q3 == '\033[1;31mX\033[1;30m' and q6 == '\033[1;31mX\033[1;30m' and q9 == '\033[1;31mX\033[1;30m':
                vitjogr1 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr1))
                sleep(4)

            elif q1 == '\033[1;31mX\033[1;30m' and q5 == '\033[1;31mX\033[1;30m' and q9 == '\033[1;31mX\033[1;30m':
                vitjogr1 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr1))
                sleep(4)
            elif q3 == '\033[1;31mX\033[1;30m' and q5 == '\033[1;31mX\033[1;30m' and q7 == '\033[1;31mX\033[1;30m':
                vitjogr1 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr1))
                sleep(4)

            elif q1 == '\033[1;31mO\033[1;30m' and q2 == '\033[1;31mO\033[1;30m' and q3 == '\033[1;31mO\033[1;30m':
                vitjogr2 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr2))
                sleep(4)
            elif q4 == '\033[1;31mO\033[1;30m' and q5 == '\033[1;31mO\033[1;30m' and q6 == '\033[1;31mO\033[1;30m':
                vitjogr2 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr2))
                sleep(4)
            elif q7 == '\033[1;31mO\033[1;30m' and q8 == '\033[1;31mO\033[1;30m' and q9 == '\033[1;31mO\033[1;30m':
                vitjogr2 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr2))
                sleep(4)

            elif q1 == '\033[1;31mO\033[1;30m' and q4 == '\033[1;31mO\033[1;30m' and q7 == '\033[1;31mO\033[1;30m':
                vitjogr2 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr2))
                sleep(4)
            elif q2 == '\033[1;31mO\033[1;30m' and q5 == '\033[1;31mO\033[1;30m' and q8 == '\033[1;31mO\033[1;30m':
                vitjogr2 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr2))
                sleep(4)
            elif q3 == '\033[1;31mO\033[1;30m' and q6 == '\033[1;31mO\033[1;30m' and q9 == '\033[1;31mO\033[1;30m':
                vitjogr2 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr2))
                sleep(4)

            elif q1 == '\033[1;31mO\033[1;30m' and q5 == '\033[1;31mO\033[1;30m' and q9 == '\033[1;31mO\033[1;30m':
                vitjogr2 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr2))
                sleep(4)
            elif q3 == '\033[1;31mO\033[1;30m' and q5 == '\033[1;31mO\033[1;30m' and q7 == '\033[1;31mO\033[1;30m':
                vitjogr2 += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31m{} GANHOU ESTA RODADA!\033[1;30m'.format(jogr2))
                sleep(4)
            elif q1 != '1' and \
                    q2 != '2' and \
                    q3 != '3' and \
                    q4 != '4' and \
                    q5 != '5' and \
                    q6 != '6' and \
                    q7 != '7' and \
                    q8 != '8' and \
                    q9 != '9':
                vitvelha += 1
                q1 = '1'
                q2 = '2'
                q3 = '3'
                q4 = '4'
                q5 = '5'
                q6 = '6'
                q7 = '7'
                q8 = '8'
                q9 = '9'
                print('\033[1;31mVelha GANHOU ESTA RODADA!\033[1;30m')
                sleep(4)

            print('\033[1;36m=-=\033[1;30m' * 25)

    # Modo: Contra bot
    elif modo == '2':
        print('\033[1;31mEm breve...\033[1;30m')
        sleep(1.5)

    # Fim do Programa
    elif modo == 'sair':
        break

    # Retorna ao Loop
    else:
        print('Não entendi.')