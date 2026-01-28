import time

while True:

    resposta = float(input('O carro estava a quantos km/h? '))
    time.sleep(0.5)
    limite = 80
    multa = (resposta - limite) * 7.0

    if resposta >= 80:
        print(f'O valor da multa é de {multa} reais.')
        time.sleep(1)
    escolha = input('Deseja calcular a multa de outro carro? (s/n) ')
    time.sleep(0.5)
    if escolha == 's':
        continue
    else:
        print('Encerrando...')
        time.sleep(1)

