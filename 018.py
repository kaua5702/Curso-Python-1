import math
import time

angulos = float(input('Digite um ângulo: '))
time.sleep(1)
angulos_radians = math.radians(angulos)

seno = math.sin(angulos_radians)
cosseno = math.cos(angulos_radians)
tangente = math.tan(angulos_radians)

print(f'O seno de {angulos}° é: {seno:.4f}')
time.sleep(1)
print(f'O cosseno de {angulos}° é: {cosseno:.4f}')
time.sleep(1)
print(f'A tangente de {angulos}° é: {tangente:.4f}')
time.sleep(1)