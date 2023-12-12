#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangete desse ângulo.
from math import cos, sin, tan
ang = float(input('Insira o valor do ângulo:'))
s = sin(ang)
c = cos(ang)
t = tan(ang)
print('Para o ângulo {} temos:/n Seno: {}/n Cosseno: {}/n Tangente: {}' .format(ang, s, c, t))
