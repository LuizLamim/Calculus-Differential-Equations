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