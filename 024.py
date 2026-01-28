nome = input('Digite o nome da sua cidade: ')
list = nome.split()
cmc = list[0]

if 'Santo' in cmc:
    print('Sua cidade começa com "santo"')
else:
    print('Sua cidade não começa com "santo"')

