import matplotlib.pyplot as plt
import numpy as np

# 1. Define o intervalo de valores para x (de -10 a 10, com 400 pontos)
x = np.linspace(-10, 10, 400)

# 2. Calcula os valores de y segundo a função f(x) = x^3 + 35
y = x**3 + 35

# 3. Cria a figura e plota a curva
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$f(x) = x^3 + 35$", color="#1f77b4", linewidth=2)

# 4. Adiciona os eixos cartesianos (x = 0 e y = 0) para referência
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")

# 5. Configurações de título, rótulos e grade
plt.title("Gráfico da função $f(x) = x^3 + 35$", fontsize=14)
plt.xlabel("Eixo X", fontsize=12)
plt.ylabel("Eixo Y", fontsize=12)
plt.grid(True, linestyle=":", alpha=0.7)
plt.legend(fontsize=12)

# 6. Exibe o gráfico na tela
plt.tight_layout()
plt.show()