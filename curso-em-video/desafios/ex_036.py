#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa.
valor_casa = float(input("Digite o valor da casa em R$:"))
#O salário do comprador:
salario = float(input("Digite o seu salário atual:"))
#E em quantos anos ele vai pagar:
anos = int(input("Digite em quantos anos você pretende pagar o empréstimo:"))
#Agora será necessário calcular o valor da prestação mensal, sabendo que ela não deve exceder 30% do salário ou então o empréstimo será negado.
quant_parcelas = (anos * 12)
valor_parcelas = (valor_casa / quant_parcelas)
if valor_parcelas <= salario * 0.3:
    print(f"O valor da prestação mensal será de {valor_parcelas:.2f}R$ dividido em {quant_parcelas} parcelas.")
else:
    print("Não é possível realizar o empréstimo desse valor.")
