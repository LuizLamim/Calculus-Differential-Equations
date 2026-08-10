import matplotlib.pyplot as plt
import numpy as np

# 1. Criar a grade de pontos no plano 2D (x, y)
x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)