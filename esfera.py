import numpy as np
import matplotlib.pyplot as plt

# Criação da figura e eixo 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Definição dos ângulos para as coordenadas esféricas
u = np.linspace(0, 2 * np.pi, 100) # phi (de 0 a 2*pi)
v = np.linspace(0, np.pi, 100)     # theta (de 0 a pi)

# Conversão para coordenadas cartesianas (Raio = 1)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Renderização da superfície da esfera
ax.plot_surface(x, y, z, color='c', alpha=0.8, edgecolor='black', linewidth=0.1)

# Ajustes visuais e proporção 1:1:1 para não distorcer a forma geométrica
ax.set_box_aspect([1, 1, 1])
ax.set_title('Esfera 3D')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Exibe o gráfico
plt.show()