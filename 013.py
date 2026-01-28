import time

salario = {
    'José': 3100,
    'Kauã': 4000,
    'Pedro': 3500,
    'Andrei': 2800,
    'Julia': 3200
}

aumento = 0.15

print(' \nBem-vindo ao sistema de consulta de salários!\n')

while True:
    time.sleep(1)
    print('Funcionários disponíveis para consulta: ')
    time.sleep(1)
    for funcionario in salario:
        print(f'-{funcionario}')
        time.sleep(1)
    print('\n')
    nome = input('Digite o nome do funcionário que deseja consultar (ou sair para encerrar): ')
    time.sleep(1)
    if nome in salario:
        salario_novo = salario[nome] * (1 + aumento)
        print('\n')
        print(f'O salário atual de(a) {nome} é R${salario[nome]}')
        time.sleep(1)
        print(f'O novo salário de {nome} é: R${salario_novo:.2f}')
        time.sleep(1)       
        resposta = input('Deseja consultar outro funcionário? (s/n): ')
        time.sleep(1)
        if resposta == 's':
            print('\n')
            print('Reiniciando programa... \n')
            time.sleep(1)
            continue
        else:
            print('Encerrando o programa...')
            time.sleep(1)
            break
    elif nome == 'sair':
        print('Encerrando o programa...')
        break
    else:
        print('Funcionário não encontrado. Tente novamente.')
        time.sleep(1)
        continue
    