import matplotlib.pyplot as plt
import numpy as np

# 1. Definir o domínio de X e Y
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)

# 2. Criar a grade bidimensional (Meshgrid)
X, Y = np.meshgrid(x, y)

# 3. Definir a função z = f(x, y)
# Exemplo: z = sin(sqrt(x^2 + y^2))
Z = np.sin(np.sqrt(X**2 + Y**2))

# 4. Criar a figura
plt.figure(figsize=(8, 6))

# Plotar as curvas de nível preenchidas
contorno_preenchido = plt.contourf(X, Y, Z, levels=20, cmap="viridis")

# Adicionar as linhas de contorno por cima para destacar
linhas = plt.contour(X, Y, Z, levels=20, colors="black", linewidths=0.5)

# Adicionar rótulos numéricos com o valor de Z em cada linha
plt.clabel(linhas, inline=True, fontsize=8, fmt="%.1f")

# Adicionar barra de cores (Colorbar)
plt.colorbar(contorno_preenchido, label="Valores de Z")

# Título e eixos
plt.title(r"Curvas de Nível: $z = \sin(\sqrt{x^2 + y^2})$")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid(True, linestyle="--", alpha=0.3)

# Exibir o gráfico
plt.tight_layout()
plt.show()