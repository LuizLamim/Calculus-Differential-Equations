import numpy as np
import matplotlib.pyplot as plt

# 1. Define o intervalo de valores para x (de -3 a 3 com 500 pontos)
x = np.linspace(-3, 3, 500)

# 2. Calcula os valores da função f(x) = e^x + sin(x)
y = np.exp(x) + np.sin(x)

# 3. Configura o gráfico
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x) = e^x + \sin(x)$', color='purple', linewidth=2)

# Adiciona linhas de eixo (x=0 e y=0)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')

# Títulos e rótulos
plt.title(r'Gráfico da Função $f(x) = e^x + \sin(x)$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=12)

# 4. Exibe o gráfico
plt.show()