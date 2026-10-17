import matplotlib.pyplot as plt
import numpy as np

# 1. Definir o intervalo de valores para X
# Selecionamos um intervalo que mostre bem o vértice e as raízes da parábola
x = np.linspace(-15, 6, 400)

# 2. Definir a função Y = 4x^2 + 35x
y = 4 * x**2 + 35 * x