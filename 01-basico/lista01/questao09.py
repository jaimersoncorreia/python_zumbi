#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule
#o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km_percorrido = float(input('Quantos Km você percorreu? '))
dias = float(input('Quantos dias permaneceu com o carro alugado? '))

preco_pagar = 60.0 * dias + 0.15 * km_percorrido

print('Você vai pagar R$ {}'.format(preco_pagar))