minutos = int(input("Minutos gastos com telefone: "))
if minutos <= 200:
	preco = 0.20
elif minutos <= 400:
	preco = 0.18
elif minutos <= 800:
	preco = 0.15
else:
	preco = 0.08

print(str("Você vai pagar R$ {:.2f}".format(minutos * preco)).replace(".", ","))
exit()