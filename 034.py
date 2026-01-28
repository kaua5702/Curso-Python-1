salario = float(input('Digite seu salário: '))

if salario >= 1250:
    aumento = salario * 0.10
    ns = salario + aumento
    print(f'Seu novo salário é {ns:.2f}')
else:
    aumento = salario * 0.15
    ns = salario + aumento
    print(f'Seu novo salário é {ns:.2f}')

