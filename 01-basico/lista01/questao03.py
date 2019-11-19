#3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
#o total em segundos.
dias = int(input('Digite a quantidade de dia: '))
horas = int(input('Digite a quantidade hora: '))
minutos = int(input('Digite a quantidade de minuto: '))
segundos = int(input('Digite a quantidade de segundos: '))


d = 24 * 60 * 60 
h = 60 * 60
minu = 60

total_de_segundos = d * dias + h * horas + minu * minutos + segundos

print(total_de_segundos)