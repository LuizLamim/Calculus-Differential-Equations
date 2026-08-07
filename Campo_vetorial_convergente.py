import numpy as np
import matplotlib.pyplot as plt

# 1. Criar a grade de pontos (X, Y) no plano cartesiano
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)