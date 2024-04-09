#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem dizendo qual dois é maior ou menor.
num_1 = int(input("Digite um número inteiro:"))
num_2 = int(input("Digite outro número inteiro:"))

if num_1 > num_2:
    print(f"O número {num_1} é maior que {num_2}.")
elif num_1 < num_2:
    print(f"O número {num_1} é menor que {num_2}.")
else:
    print("Os dois números digitados são iguais.")

print("Fim do programa.")
