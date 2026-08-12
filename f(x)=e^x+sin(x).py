import numpy as np
import matplotlib.pyplot as plt

# 1. Define o intervalo de valores para x (de -3 a 3 com 500 pontos)
x = np.linspace(-3, 3, 500)

# 2. Calcula os valores da função f(x) = e^x + sin(x)
y = np.exp(x) + np.sin(x)