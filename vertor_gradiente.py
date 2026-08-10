import matplotlib.pyplot as plt
import numpy as np

# 1. Criar a grade de pontos no plano 2D (x, y)
x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)

# 2. Definir a função escalar f(x, y)
# Exemplo: f(x, y) = x² + y² (um paraboloide)
Z = X**2 + Y**2