import numpy as np
import matplotlib.pyplot as plt

# Define o intervalo de valores para x (de -10 a 10, com 400 pontos para uma curva suave)
x = np.linspace(-10, 10, 400)

# Define a função y = |x| + 3
y = np.abs(x) + 3

# Cria o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = |x| + 3', color='blue', linewidth=2)

# Adiciona título e rótulos aos eixos
plt.title('Gráfico da função f(x) = |x| + 3')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')

# Adiciona uma grade para facilitar a visualização
plt.grid(True, linestyle='--', alpha=0.7)

# Destaca os eixos x e y em preto
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Mostra a legenda
plt.legend()

# Exibe o gráfico
plt.show()