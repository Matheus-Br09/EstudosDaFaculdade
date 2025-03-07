price_n1 = float(input('Valor do 1° Produto: R$'))
price_n2 = float(input('Valor do 2° Produto: R$'))
price_n3 = float(input('Valor do 3° Produto: R$'))

min_price = min(price_n1, price_n2, price_n3)
print(f'Você levou o produto por R${min_price} ')

