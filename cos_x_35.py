import matplotlib.pyplot as plt
import numpy as np

# 1. Define o intervalo de valores para x (ex: de -2π a 2π)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 2. Calcula a função y = cos(x) + 35
y = np.cos(x) + 35

# 3. Configura a figura do gráfico
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=r"$f(x) = \cos(x) + 35$", color="indigo", linewidth=2)

# 4. Personalização das marcas do eixo X em termos de Pi (π)
ticks_x = np.array([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]) * np.pi
labels_x = [
    r"$-2\pi$",
    r"$-3\pi/2$",
    r"$-\pi$",
    r"$-\pi/2$",
    "$0$",
    r"$\pi/2$",
    r"$\pi$",
    r"$3\pi/2$",
    r"$2\pi$",
]
plt.xticks(ticks_x, labels_x)

# 5. Títulos, legendas e grade
plt.title(r"Gráfico da Função $f(x) = \cos(x) + 35$", fontsize=14, pad=15)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=12, loc="upper right")

# Ajusta os limites do eixo Y para destacar o deslocamento vertical
plt.ylim(33.5, 36.5)

# 6. Exibe o gráfico
plt.tight_layout()
plt.show()