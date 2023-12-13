#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangete desse ângulo.
from math import cos, sin, tan
ang = float(input('Insira o valor do ângulo:'))
print('Para o ângulo {:.1f} temos:\n Seno: {:.2f}\n Cosseno: {:.2f}\n Tangente: {:.2f}' .format(ang, sin(ang), cos(ang), tan(ang)))
