numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
if numero1 > numero2:
    print(f'O maior é o primeiro valor: {numero1}')
elif numero2 > numero1:
    print(f'O maior é o segundo valor: {numero2}')
else:
    print('Os dois são iguais')
