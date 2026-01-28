km = float(input('Digite em km a distância da viagem: '))

if km <= 200:
    valor = km * 0.50
    print(f'O valor da passagem é de R${valor:.2f}')

else:
    valor = km * 0.45
    print(f'O valor da passagem é de R${valor:.2f}')