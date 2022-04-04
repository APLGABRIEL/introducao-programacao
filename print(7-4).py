# PROGRAMA TEMPERATURA – O usuário digita a temperatura em graus Célsius e o programa exibe o valor em graus Fahrenheit.
#  A conversão é dada pela seguinte fórmula: F = C * 1,8 + 32
  
from sys import float_repr_style


c = float(input("digite a temeratura: "))
valor1 = (c * 1.8) + 32
print(f" Célsius {c} é = {valor1} em Fahrenheit!")