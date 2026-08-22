import numpy as np
import matplotlib.pyplot as plt

# 1. Cria a figura e o eixo 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 2. Define o intervalo para as coordenadas x e y (de -10 a 10)
x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)