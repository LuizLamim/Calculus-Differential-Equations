import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Configuração da figura e do eixo 3D
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")

# Parâmetros geométricos do cone
R = 2.0  # Raio da base do cone
H = 4.0  # Altura do cone