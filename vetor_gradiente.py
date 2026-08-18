import matplotlib.pyplot as plt
import numpy as np

# 1. Definir a grade de pontos (x, y)
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# 2. Definir a função escalar f(x, y)
# Exemplo: f(x, y) = x^2 + y^2
Z = X**2 + Y**2