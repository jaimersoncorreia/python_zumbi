#4) Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

salario = float(input('Informe um salário: '))
porcentagem = float(input('Informe o percentual de aumento: ')) / 100

salario += salario * porcentagem
print('{}'.format(salario))