import random
import time

saldo = random.randint(500, 5000)

print('\n Bem vindo ao Banco Itaú \n')
time.sleep(1)

while True:
    print('Escolha uma das opções abaixo: \n')
    time.sleep(1)
    print('[1] Depositar')
    time.sleep(1)
    print('[2] Sacar')
    time.sleep(1)
    print('[3] Extrato')
    time.sleep(1)
    print('[4] Dólar')
    time.sleep(1)
    print('[5] Sair \n')

    escolha = int(input('Digite a opção desejada: '))
    time.sleep(1)

    if escolha == 1:
        valor = input('Digite o valor que deseja depositar: R$ ')
        time.sleep(1)
        print(f'Você depositou R${valor} com sucesso! \n')
        time.sleep(1)
        print(f'Seu novo saldo é de R${saldo + float(valor)}')
        time.sleep(1)
        resposta = input('Deseja realizar outra operação? [S/N]: ')
        time.sleep(1)
        if resposta == 'S':
            print('Reiniciando... \n')
            time.sleep(1)        
            continue
        else:
            print('Obrigado por usar nosssos serviços. Volte sempre!')
            time.sleep(1)
            print('Encerrando...')
            break
    
    elif escolha == 2:
        valor = input('Digite o valor que deseja sacar: R$ ')
        time.sleep(1)       
        print(f'Você sacou R${valor} com sucesso! \n')
        time.sleep(1)
        print(f'Seu novo saldo é de R${saldo - float(valor)}')
        time.sleep(1)
        resposta = input('Deseja realizar outra operação? [S/N]: ')
        time.sleep(1)
        if resposta == 'S':
            print('Reiniciando... \n')
            time.sleep(1)
            continue
        else:
            print('Obrigado por usar nossos serviços. Volte sempre!')    
            time.sleep(1)
            print('Encerrando...')
            time.sleep(1)
            break

    elif escolha == 3:
        print(f"Seu saldo atual é de R${saldo}")
        time.sleep(1)
        resposta = input('Deseja realizar outra operação? [S/N]: ')
        time.sleep(1)
        if resposta == 'S':
            print('Reiniciando... \n')
            time.sleep(1)
            continue
        else:
            print('Obrigado por usar nossos serviços. Volte sempre!')
            print('Encerrando...')
            break


    elif escolha == 4:
        dolar = saldo / 3.27
        print(f'Seu saldo em dólar é de U${dolar:.2f}')
        resposta = input('Deseja realizar outra operação? [S/N]: ')
        if resposta == 'S':
            print('Reiniciando... \n')
            continue
        else:
            print('Obrigado por usar nossos serviços. Volte sempre!')
            time.sleep(1)
            print('Encerrando...')
            time.sleep(1)
            break
        

    if escolha == 5:
        print('Obrigado por usar nossos serviços. Volte sempre!')
        time.sleep(1)
        print('Encerrando...')
        time.sleep(1)
        break