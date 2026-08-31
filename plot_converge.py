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