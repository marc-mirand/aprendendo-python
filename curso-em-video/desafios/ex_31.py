#Desenvolva um programa que pergunte a distância em Km.
distancia = float(input("Qual será a distancia da viagem em Km?"))

#Calcule o preço da passagem, cobrando R$ 0.50 por km para viagens de até 200km e R$ 0.45 para viagens mais longas.
if distancia <= 200:
    preco = distancia * 0.50
    print(f"O valor da passagem será: R${preco}")
else:
    preco = distancia * 0.45
    print(f"O valor da passagem será: R${preco}")
