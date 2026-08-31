import matplotlib.pyplot as plt
import numpy as np

# 1. Criação da grade de pontos (x, y)
x = np.linspace(-5, 5, 15)
y = np.linspace(-5, 5, 15)
X, Y = np.meshgrid(x, y)

# 2. Definição das componentes do campo vetorial convergente
# As componentes negativas apontam em direção à origem (0, 0)
U = -X
V = -Y

# 3. Criação do gráfico
plt.figure(figsize=(8, 8))

# O 'quiver' plota os vetores. Normalizamos o tamanho para melhor visualização.
plt.quiver(X, Y, U, V, color="crimson", angles="xy", scale_units="xy", scale=2.5)

# 4. Configurações visuais do gráfico
plt.title("Campo Vetorial Convergente: $\\vec{F}(x,y) = -x\\hat{i} - y\\hat{j}$")
plt.xlabel("X")
plt.ylabel("Y")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(True, linestyle=":", alpha=0.6)
plt.xlim(-6, 6)
plt.ylim(-6, 6)

# Exibe o gráfico
plt.show()