num_1 = int(input('Primeiro valor: '))
num_2 = int(input('Segundo valor: '))
num_3 = int(input('Terceiro valor: '))
numeros = [num_1, num_2, num_3]
numeros.sort(reverse=True)
print(f'{numeros[0]} - {numeros[1]} - {numeros[2]}')
