altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
tinta = area / 2

print(f'Sua parede tem {altura} m de altura e {largura} m de largura, totalizando uma área de {area} m²')
print(f'Logo para pintar essa parede, você precisará de {tinta}L de tinta')