#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para que o usuário tente descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador = randint(0,5)

usuario = int(input("Digite um número de 0 a 5 que você acha que o computador escolheu:"))

if computador == usuario:
    print("Parabéns! Você acertou!")
else:
    print(f"Você errou, o número escolhido foi: {computador}")
