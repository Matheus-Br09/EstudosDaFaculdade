from math import *

cat_oposto = float(input('Cateto Oposto: '))
cat_adj = float(input('Cateto Adjacente: '))
hipotenusa = hypot(cat_oposto, cat_adj)
print(f'A hipotenusa do triângulo é: {hipotenusa:.2f}')