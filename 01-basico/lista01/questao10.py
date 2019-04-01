'''
10) Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos
dias de vida um fumante perderá. Exiba o total de dias.
'''

cigarros_por_dia = int(input('Quantos cigarros fuma por dia? '))
anos = int(input('Por quantos anos você fumou? '))

qtde_cigarro = cigarros_por_dia * anos * 365
minutos_perdidos = qtde_cigarro * 10
horas_perdidas = minutos_perdidos / 60
dias_perdidos = horas_perdidas // 24
print('\nVocê fumou {} cigarros em {} anos.'.format(qtde_cigarro, anos))
print('Você perdeu aproximadamente {} dias da sua vida por causa do cigarro.'.format(dias_perdidos))