valor_produto = float(input('Digite o valor de um produto: R$'))
desc_produto = valor_produto - (valor_produto * (5/100))
print(f'O valor original do produto é: R${valor_produto:.2f}')
print(f'Com o desconto de 5% ele passa a valer: R${desc_produto: .2f}')
