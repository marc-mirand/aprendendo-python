# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0,15 por Km rodado.
k = float(input('Insira a quilometragem percorrida:'))
d = int(input('Agora insira por quantos dias o carro foi usado:'))
p = (d * 60) + (k * 0.15)
print('O cliente usou o carro por {} dias e rodou {} quilometros, sendo assim ele deverá pagar {:.2f} R$.'.format(d, k, p))
