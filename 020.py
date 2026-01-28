import random
import time

nomes = {
    'Kauã': 1,
    'Pedro': 2,
    'Andrei': 3,
    'José': 4,
}

lista_nomes = list(nomes.keys())
random.shuffle(lista_nomes)

print('Ordem de apresentação:')
time.sleep(1)
for i, nome in enumerate(lista_nomes, start = 1):
    print(f'{i}° - {nome}')
    time.sleep(1)