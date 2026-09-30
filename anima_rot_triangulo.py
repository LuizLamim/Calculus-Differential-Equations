import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Configuração da figura e do eixo 3D
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")

# Parâmetros geométricos do cone
R = 2.0  # Raio da base do cone
H = 4.0  # Altura do cone

# Configuração inicial dos limites do gráfico 3D
def setup_axis(ax):
  ax.set_xlim([-2.5, 2.5])
  ax.set_ylim([-2.5, 2.5])
  ax.set_zlim([0, 4.5])
  ax.set_xlabel("Eixo X")
  ax.set_ylabel("Eixo Y")
  ax.set_zlabel("Eixo Z")

# Número de quadros da animação
num_frames = 120
angles = np.linspace(0, 2 * np.pi, num_frames)

def update(frame):
  ax.clear()
  setup_axis(ax)
  
  theta = angles[frame]
  graus = int(np.degrees(theta))
  ax.set_title(f"Formação de um Cone por Rotação (Ângulo: {graus}°)", fontsize=13)

  # 1. Desenhar a superfície do cone acumulada até o ângulo atual
  if frame > 0:
    t_vals = np.linspace(0, theta, max(2, int(frame * 25 / num_frames)))
    r_vals = np.linspace(0, R, 15)
    T, R_grid = np.meshgrid(t_vals, r_vals)
    X = R_grid * np.cos(T)
    Y = R_grid * np.sin(T)
    Z = H * (1 - R_grid / R) # Altura decresce do ápice até a base
    
    ax.plot_surface(X, Y, Z, color='cyan', alpha=0.5, edgecolor='none', shade=True)

  # 2. Desenhar o triângulo na posição atual de rotação
  # Vértices: Ápice (0,0,H), Origem inferior (0,0,0), Ponto na base (R*cos(theta), R*sin(theta), 0)
  tri_x = [0, 0, R * np.cos(theta), 0]
  tri_y = [0, 0, R * np.sin(theta), 0]
  tri_z = [H, 0, 0, H]

  ax.plot(tri_x, tri_y, tri_z, color='red', linewidth=2.5, marker='o')

  # 3. Desenhar o eixo central de rotação (Eixo Z)
  ax.plot([0, 0], [0, 0], [0, H], color='black', linestyle='--', alpha=0.6)

  return ax

# Criar a animação
ani = FuncAnimation(fig, update, frames=num_frames, interval=40, blit=False)

# Exibir a janela com a animação
plt.show()