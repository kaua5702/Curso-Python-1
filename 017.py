import math
import time

catetoop = float(input('Digite o valor do cateto oposto: ' ))
time.sleep(1)
catetoadj = float(input('Digite o valor do cateto adjacente: '))
time.sleep(1)
hipotenusa = math.hypot(catetoop, catetoadj)

print(f'o valor da hipotenusa é {hipotenusa}')
time.sleep(1)