#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 - binário; 2 - octal; 3 - hexadecimal.
numero = int(input("Digite um número inteiro:"))
base = int(input("Digite para qual base deverei convertê-lo: \n[1] Binário; \n[2] Octal; \n[3] Hexadecimal;"))

if base == 1:
    numero = bin(numero)
    print(numero[2:])
elif base == 2:
    numero = oct(numero)
    print(numero[2:])
elif base == 3:
    numero = hex(numero)
    print(numero[2:])
else:
    print("OPÇÃO INVÁLIDA!")

print("Fim do programa.")
