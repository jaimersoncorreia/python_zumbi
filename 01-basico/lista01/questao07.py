#7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

c = float(input('Informe a temperatura em Celsius: '))
f = 9*c/5 + 32
print('{}°C = {}°F'.format(c,f))