#5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
#preço a pagar.

preco = float(input('Valor da mercadoria: '))
desconto = float(input('Percentual de desconto: ')) / 100
a_pagar = preco - preco * desconto
print('Valor do desconto: R$ {}'.format(preco * desconto))
print('Valor a pagar: R$ {}'.format(a_pagar))