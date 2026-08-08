import numpy as np
import matplotlib.pyplot as plt

# 1. Definindo o espaço (grid)
x = np.linspace(-5, 5, 20) # Cria 20 pontos de -5 a 5 no eixo X
y = np.linspace(-5, 5, 20) # Cria 20 pontos de -5 a 5 no eixo Y
X, Y = np.meshgrid(x, y)   # Cria uma malha 2D com esses pontos