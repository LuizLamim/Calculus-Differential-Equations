import matplotlib.pyplot as plt
import numpy as np

# 1. Cria uma matriz 3x3 preenchida com zeros
matriz = np.zeros((3, 3))

# 2. Configura a exibição da matriz
plt.figure(figsize=(5, 5))
plt.imshow(matriz, cmap='Blues', vmin=0, vmax=1)

# 3. Adiciona as divisões da grade (grid)
plt.grid(True, color='gray', linestyle='-', linewidth=1.5)

# 4. Ajusta os eixos para mostrar os índices de 0 a 2
plt.xticks(np.arange(-0.5, 3, 1), labels=['', '', '', ''])
plt.yticks(np.arange(-0.5, 3, 1), labels=['', '', '', ''])
plt.tick_params(length=0) # Esconde os traços dos eixos