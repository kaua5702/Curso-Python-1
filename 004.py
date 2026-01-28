import time

algo = input("Digite algo: ")

print('O tipo primitivo desse valor é', type(algo))
time.sleep(1.5)   
print(f'{algo} é uma palavra/letra' if algo.isalpha() else f'{algo} não é uma palavra/letra')
time.sleep(1.5)   
print(f'{algo} é um número' if algo.isnumeric() else f'{algo} não é um número')
time.sleep(1.5) 
print(f'{algo} é alfanumérico' if algo.isalnum() else f'{algo} não é alfanumérico')
time.sleep(1.5)
print(f'{algo} esta em maisculo' if algo.isupper() else f'{algo} não esta em maisculo')
time.sleep(1.5)
print(f'{algo} é um espaço' if algo.isspace() else f'{algo} não é um espaço')
time.sleep(1.5)