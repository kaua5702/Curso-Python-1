nome = input('Digite seu nome completo: ')
partes = nome.split()
fn = partes[0]
ln = partes[-1]

print(f'Seu primeiro nome é: {fn}')
print(f'Seu último nome é: {ln}')
