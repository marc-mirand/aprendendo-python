#Escreva um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))
num3 = int(input("Por fim, digite outro número inteiro:"))

escolhidos = [num1, num2, num3]

print(f"O maior número digitado foi: {max(escolhidos)} e o menor foi {min(escolhidos)}.")
