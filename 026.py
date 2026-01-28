f = input('Digite uma frase: ')
a = f.lower().count('a')
p = f.lower().find('a')
p2 = f.lower().rfind('a')

print(f'Sua frase tem {a} "a" ')
print(f'O primeiro "a" está na posição {p + 1}')
print(f'O último "a" está na posição {p2 - 1}')