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

# 4. Adiciona linhas dos eixos X e Y para referência
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")

# 5. Configurações visuais (título, rótulos, grade e legenda)
plt.title("Gráfico da Função Exponencial")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True, which="both", linestyle=":", alpha=0.7)
plt.legend(fontsize=12)

# 6. Exibe o gráfico na tela
plt.show()