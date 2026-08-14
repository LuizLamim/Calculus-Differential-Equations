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