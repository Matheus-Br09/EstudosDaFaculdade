from math import *

valor_angulo = float(input('Digite o ângulo: '))
seno_val = sin(radians(valor_angulo))
cos_val = cos(radians(valor_angulo))
tang_val = tan(radians(valor_angulo))

print(f'Valor digitado: {valor_angulo}°')
print(f'Seno: {seno_val:.2f}°')
print(f'Cosseno: {cos_val:.2f}')
print(f'Tangente: {tang_val:.2f}')