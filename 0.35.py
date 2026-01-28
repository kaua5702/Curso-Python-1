a = float(input('Digite o cumprimento da linha a: '))
b = float(input('Digite o cumprimento da linha b: '))
c = float(input('Digite o cumprimento da linha c: '))

if a + b > c and a + c > b and b + c > a:
    print('As linhas podem formar um triângulo!')
else:
    print('As linhas não fazem um triângulo.')