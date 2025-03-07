num1 = int(input('Digite o 1° valor: '))
num2 = int(input('Digite o 2° valor: '))
num3 = int(input('Digite o 3° valor: '))

print('=='*14)
if num1 > num2 > num3:
    print(f'Maior: {num1} \nMenor: {num3}')
elif num1 > num3 > num2:
    print(f'Maior: {num1} \nMenor: {num2}')
if num2 > num1 > num3:
    print(f'Maior: {num2} \nMenor: {num3}')
elif num2 > num3 > num1:
    print(f'Maior: {num2} \nMenor: {num1}')
if num3 > num2> num1:
    print(f'Maior: {num3} \nMenor: {num1}')
elif num3 > num1 > num2:
    print(f'Maior: {num3} \nMenor: {num2}')
