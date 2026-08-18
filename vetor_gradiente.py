import matplotlib.pyplot as plt
import numpy as np

# 1. Definir a grade de pontos (x, y)
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# 2. Definir a função escalar f(x, y)
# Exemplo: f(x, y) = x^2 + y^2
Z = X**2 + Y**2

# 3. Calcular o Vetor Gradiente (df/dx, df/dy)
# O gradiente analítico de x^2 + y^2 é (2x, 2y)
# Também podemos usar np.gradient para calcular numericamente:
U, V = np.gradient(Z, x[1] - x[0], y[1] - y[0])

# 4. Configurar a figura
fig, ax = plt.subplots(figsize=(8, 7))

# Desenhar as curvas de nível (contorno) da função
contour = ax.contour(X, Y, Z, levels=15, cmap="viridis", alpha=0.5)
fig.colorbar(contour, label="Valor da função f(x, y)")

# Plotar o Vetor Gradiente usando 'quiver'
# Os vetores apontam na direção de maior subida
ax.quiver(
    X,
    Y,
    U,
    V,
    color="red",
    angles="xy",
    scale_units="xy",
    scale=5,
    label="Vetor Gradiente",
)

# Estilização do gráfico
ax.set_title(r"Vetor Gradiente de $f(x, y) = x^2 + y^2$", fontsize=14)
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend(loc="upper right")
ax.set_aspect("equal")

# Exibir o gráfico
plt.show()