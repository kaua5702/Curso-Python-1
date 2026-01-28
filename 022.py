import time

nome = input('Digite seu nome completo: ').strip()
time.sleep(1)
n_s_e = nome.replace(' ', '')
nl = len(n_s_e)
fn = nome.split()
c = len(fn[0])
n = fn[0]

print(f'Seu nome em letras maíusculas fica: {nome.upper()}')
time.sleep(1)
print(f'Seu nome em letras minúsculas fica: {nome.lower()}')
time.sleep(1)
print(f'Seu nome tem {nl} letras.')
time.sleep(1)
print(f'Seu primeiro nome é {n} e tem {c} letras')
time.sleep(1)
