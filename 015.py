dias = float(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos km rodados? ')) 
v1 = dias * 60
v2 = km * 0.15
total = v1 + v2

print(f'O valor diário ficou R${v1:.2f}')
print(f'O valor por km ficou R${v2:.2f}')
print(f'O valor total ficou R${total:.2f}')
