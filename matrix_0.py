import matplotlib.pyplot as plt
import numpy as np

# 1. Cria uma matriz 3x3 preenchida com zeros
matriz = np.zeros((3, 3))

# 2. Configura a exibição da matriz
plt.figure(figsize=(5, 5))
plt.imshow(matriz, cmap='Blues', vmin=0, vmax=1)