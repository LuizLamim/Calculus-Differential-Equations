import matplotlib.pyplot as plt
import numpy as np

# 1. Define o intervalo de valores para o eixo X (de -5 a 2, com 400 pontos)
x = np.linspace(-5, 2, 400)

# 2. Define a função f(x) = 5^(x + 2)
# Nota: Se você quiser f(x) = (5^x) + 2, altere a linha abaixo para: y = (5 ** x) + 2
y = 5 ** (x + 2)

# 3. Cria a figura e plota o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$f(x) = 5^{x+2}$", color="blue", linewidth=2)