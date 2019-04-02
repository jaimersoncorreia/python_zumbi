minutos = int(input("Minutos gastos com telefone: "))
if minutos <= 200:
	preco = 0.20
else:
	if minutos <= 400:
		preco = 0.18
	else:
		if minutos <= 800:
			preco = 0.15
		else:
			preco = 0.08

print(str("Você vai pagar R$ {:.2f}".format(minutos * preco)).replace(".", ","))
exit()
velocidade = float(input("Qual a velocidade do carro: "))
if velocidade > 110:
	valor_muta = (velocidade - 110) * 5
	reais = str("Você foi multado em R$ {:.2f}!".format(valor_muta)).replace(".",",")
	print(reais)