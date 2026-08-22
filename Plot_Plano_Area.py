import numpy as np
import matplotlib.pyplot as plt

# 1. Cria a figura e o eixo 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 2. Define o intervalo para as coordenadas x e y (de -10 a 10)
x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)

# 3. Define a equação do plano: z = 2x + 3y - 5
Z = 2*X + 3*Y - 5

# 4. Plota a superfície do plano
# O parâmetro 'alpha' controla a transparência e 'cmap' a paleta de cores
plano = ax.plot_surface(X, Y, Z, alpha=0.8, cmap='viridis', edgecolor='k', linewidth=0.1)

# Adiciona uma barra de cores para referência visual
fig.colorbar(plano, ax=ax, shrink=0.5, aspect=10, label='Valor de Z')

# 5. Configura os rótulos e o título
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')
ax.set_title('Plano: 2x + 3y - z = 5')

# 6. Exibe o gráfico interativo
plt.show()