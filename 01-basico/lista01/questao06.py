#6) Calcule o tempo de uma viagem de carro. 
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = float(input('Informe a distância em km: '))
velocidade = float(input('Informe a velocidade km/h: '))

tempo_de_viagem = distancia / velocidade

print('O tempo de viagem é {}h'.format(tempo_de_viagem))