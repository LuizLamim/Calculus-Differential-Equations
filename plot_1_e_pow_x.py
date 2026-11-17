import matplotlib.pyplot as plt
import numpy as np

# 1. Define o intervalo de valores para x (de -3 a 5, com 400 pontos para suavidade)
x = np.linspace(-3, 5, 400)

# 2. Calcula os valores de y = 1 / e^x
y = 1 / np.exp(x)