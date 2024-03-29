#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7.00 por cada Km acima do limite.

quilometro = int(input("Digite a velocidade do carro:"))

if quilometro > 80:
    multa = (quilometro - 80) * 7
    print(f"Você estava acima da velocidade permitida e deverá pagar uma multa de R${multa}")
else:
    print("Você estava dentro da velocidade permitida.")
