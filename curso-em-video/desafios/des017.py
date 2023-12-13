# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Insira o cateto oposto:'))
ca = float(input('Insira o cateto adjacente:'))
print('O triangulo retângulo que possui o cateto oposto {} e o cateto adjacente {} possui a hipotenusa {}.' .format(co, ca, hypot(co, ca)))
