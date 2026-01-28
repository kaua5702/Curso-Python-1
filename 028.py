import random
import time

print('  Bem vindo ao jogo de adivinhação!\n')
time.sleep(0.5)
print(' Seu objetivo é acertar o número que o computador escolher!!\n')
time.sleep(0.5)

while True:

    e_pc = random.randint(1, 5)
    e_us = int(input('Digite um número de 1 a 5: '))
    time.sleep(1)

    if e_us == e_pc:
        print('Parabens você acertou!')
        time.sleep(0.5)
        resposta = input('Vamos de novo? (s/n) ')
        time.sleep(1)
        if resposta == 's':
            continue
        else:
            print('Ok, até outro dia.')
            time.sleep(1)
            print('Encerrando...')
            time.sleep(1)
            break
    else:
        print('Não foi dessa vez!')
        time.sleep(0.5)
        resposta = input('Vamos de novo? (s/n) ')
        time.sleep(1)
        if resposta == 's':
            continue
        else:
            print('Ok, até outro dia.')
            time.sleep(1)
            print('Encerrando...')
            time.sleep(1)
            break
