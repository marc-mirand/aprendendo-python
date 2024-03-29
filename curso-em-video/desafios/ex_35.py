#Escreva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
reta_1 = float(input("Digite o valor da primeira reta:"))
reta_2 = float(input("Digite o valor da segunda reta:"))
reta_3 = float(input("Digite o valor da terceira reta:"))

if (reta_1 + reta_2 > reta_3) and (reta_1 + reta_3 > reta_2) and (reta_2 + reta_3 > reta_1):
    print(f"Com as retas {reta_1}, {reta_2} e {reta_3} é possivel formar um triângulo.")
else:
        print(f"Com as retas {reta_1}, {reta_2} e {reta_3} é impossivel formar um triângulo.")
