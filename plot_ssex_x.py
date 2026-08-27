import matplotlib.pyplot as plt
import numpy as np

# Definindo o intervalo de x (ex: de -2π a 2π)
x = np.linspace(-2 * np.pi, 2 * np.pi, 2000)

# Calculando a secante e aplicando o valor absoluto |sec(x)|
y = np.abs(1 / np.cos(x))

# Removendo descontinuidades (assíntotas) para não desenhar linhas verticais falsas
y[y > 10] = np.nan

# Configurando o tamanho da figura
plt.figure(figsize=(10, 6))

# Plotando a função |sec(x)|
plt.plot(x, y, label=r'$y = |\sec(x)|$', color='crimson', linewidth=2)

# Adicionando linhas das assíntotas verticais nos múltiplos de π/2
assintotas = [-1.5 * np.pi, -0.5 * np.pi, 0.5 * np.pi, 1.5 * np.pi]
for a in assintotas:
  plt.axvline(x=a, color='gray', linestyle='--', alpha=0.7)

# Ajustes dos eixos e rótulos
plt.ylim(0, 6)
plt.xlim(-2 * np.pi, 2 * np.pi)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Rótulos dos eixos X com múltiplos de π
plt.xticks(
    [-2 * np.pi, -1.5 * np.pi, -np.pi, -0.5 * np.pi, 0, 0.5 * np.pi, np.pi, 1.5 * np.pi, 2 * np.pi],
    [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
)

# Título, legenda e grade
plt.title(r'Gráfico da Função $y = |\sec(x)|$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right', fontsize=12)

# Exibir o gráfico
plt.show()