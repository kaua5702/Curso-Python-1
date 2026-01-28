nome = input('Digite seu nome completo: ').strip()
list = nome.lower().split()

if 'silva' in list:
    print('Seu nome tem Silva')
else:
    print('Seu nome não tem Silva')