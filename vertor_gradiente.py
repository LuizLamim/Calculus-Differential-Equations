import matplotlib.pyplot as plt
import numpy as np

# 1. Criar a grade de pontos no plano 2D (x, y)
x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)

# 2. Definir a função escalar f(x, y)
# Exemplo: f(x, y) = x² + y² (um paraboloide)
Z = X**2 + Y**2

# 3. Calcular o gradiente numericamente: ∇f = (df/dx, df/dy)
# Nota: np.gradient retorna primeiro a variação no eixo vertical (y) e depois no horizontal (x)
dF_dy, dF_dx = np.gradient(Z, y[1] - y[0], x[1] - x[0])

# 4. Configurar a figura
plt.figure(figsize=(8, 6))

# Plotar as curvas de nível da função f(x, y)
contornos = plt.contour(X, Y, Z, levels=15, cmap="viridis", alpha=0.6)
plt.clabel(contornos, inline=True, fontsize=8)

# Plotar os vetores gradiente usando plt.quiver
plt.quiver(
    X,
    Y,
    dF_dx,
    dF_dy,
    color="crimson",
    angles="xy",
    scale_units="xy",
    scale=12,
    headwidth=3.5,
)

# Detalhes visuais do gráfico
plt.title(
    r"Campo de Vetores Gradiente de $f(x, y) = x^2 + y^2$", fontsize=12, pad=12
)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.axhline(0, color="gray", linewidth=0.8, linestyle="--")
plt.axvline(0, color="gray", linewidth=0.8, linestyle="--")
plt.grid(True, linestyle=":", alpha=0.5)
plt.axis("equal")

# Exibir o gráfico
plt.show()