#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

numero = int(input("Digite um número inteiro:"))

if numero % 2 == 0:
    print(f"O número digitado: {numero} é par!")
else:
    print(f"O número digitado: {numero} é impar!")
