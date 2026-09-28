import numpy as np
import matplotlib.pyplot as plt

# Gera valores de x maiores que 0 (já que o log não existe para x <= 0)
# Começamos de 0.1 até 10 com 400 pontos para a curva ficar suave
x = np.linspace(0.1, 10, 400)

# Calcula as funções logarítmicas
y_natural = np.log(x)   # Logaritmo natural (base e)
y_base10 = np.log10(x)  # Logaritmo na base 10

# Criação do gráfico
plt.figure(figsize=(8, 5))

# Plota as curvas
plt.plot(x, y_natural, label="ln(x) [Base e]", color="blue", linewidth=2)
plt.plot(x, y_base10, label="log10(x) [Base 10]", color="orange", linewidth=2, linestyle="--")

# Configurações visuais do gráfico
plt.title("Gráfico de Funções Logarítmicas", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.axhline(0, color="black", linewidth=1, linestyle="--") # Linha do eixo X
plt.axvline(0, color="black", linewidth=1, linestyle="--") # Linha do eixo Y
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(fontsize=11)

# Exibe o gráfico
plt.show()