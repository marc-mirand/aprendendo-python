#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250.00, calcule o aumento de 10%.
#Para os inferiores ou iguais o aumento é de 15%.

salario = float(input("Digite o valor do seu salário atual:"))
if salario > 1250:
    aumento = 0.10 * salario
    novo_salario = aumento + salario
    print(f"Seu aumento será de R${aumento:.2f} e seu novo salário será: R${novo_salario:2}")
else:
    aumento = 0.15 * salario
    novo_salario = aumento + salario
    print(f"Seu aumento será de R${aumento:.2f} e seu novo salário será: R${novo_salario:2}")
