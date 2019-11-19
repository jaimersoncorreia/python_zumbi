velocidade = float(input("Qual a velocidade do carro: "))
if velocidade > 110:
	valor_muta = (velocidade - 110) * 5
	reais = str('Você foi multado em R$ {:.2f}!'.format(valor_muta)).replace('.',',')
	print(reais)


exit(0)
print("Teste #02")
idade = int(input("Digite a idade de seu carro: "))
if idade <= 2:
	print("Seu carro é novo!")
if idade > 3:
	print('Seu carro é velho!')


print("Teste #01")
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
	print('O promerio número é o maior!')
if b > a:
	print('O segundo número é maior!')

