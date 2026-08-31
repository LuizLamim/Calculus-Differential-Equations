import matplotlib.pyplot as plt
import numpy as np

# 1. Criação da grade de pontos (x, y)
x = np.linspace(-5, 5, 15)
y = np.linspace(-5, 5, 15)
X, Y = np.meshgrid(x, y)