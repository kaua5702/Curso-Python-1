import time

numero = int(input('Digite um número inteiro: '))
time.sleep(1)
print('\n')
print(f'A tabuada de {numero} é: \n')
time.sleep(1)
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')