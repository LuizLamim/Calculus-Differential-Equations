import matplotlib.pyplot as plt
import numpy as np

# 1. Definir o intervalo de valores para X
# Selecionamos um intervalo que mostre bem o vértice e as raízes da parábola
x = np.linspace(-15, 6, 400)

# 2. Definir a função Y = 4x^2 + 35x
y = 4 * x**2 + 35 * x

# 3. Criar a figura e o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r"$f(x) = 4x^2 + 35x$", color="blue", linewidth=2)

# 4. Destacar pontos importantes
# Raízes: (0,0) e (-8.75, 0)
# Vértice: Xv = -35 / (2*4) = -4.375, Yv = f(-4.375) = -76.5625
xv = -35 / 8
yv = 4 * (xv**2) + 35 * xv

plt.plot(
    [0, -8.75],
    [0, 0],
    "ro",
    label="Raízes: $(0, 0)$ e $(-8.75, 0)$",
    markersize=7,
)
plt.plot(
    xv,
    yv,
    "go",
    label=f"Vértice: $({xv:.2f}, {yv:.2f})$",
    markersize=7,
)

# 5. Personalizar o gráfico (linhas dos eixos, títulos e legenda)
plt.axhline(0, color="black", linewidth=1)  # Eixo X
plt.axvline(0, color="black", linewidth=1)  # Eixo Y
plt.grid(True, linestyle="--", alpha=0.6)

plt.title("Gráfico da Função Quadrática $f(x) = 4x^2 + 35x$", fontsize=14)
plt.xlabel("X", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.legend(fontsize=11)

# 6. Exibir o gráfico
plt.show()