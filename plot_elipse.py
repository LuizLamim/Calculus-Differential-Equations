import matplotlib.pyplot as plt
import numpy as np

# Parâmetros da elipse
h, k = 0, 0  # Centro da elipse (h, k)
a = 18        # Semieixo maior (horizontal)
b = 7        # Semieixo menor (vertical)

# Ângulo t variando de 0 a 2π
t = np.linspace(0, 2 * np.pi, 500)

# Equações paramétricas da elipse
x = h + a * np.cos(t)
y = k + b * np.sin(t)

# Configuração do gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'Elipse: a={a}, b={b}', color='blue', linewidth=2)
plt.plot(h, k, 'ro', label='Centro (0,0)')  # Plota o ponto do centro

# Ajustes dos eixos e visualização
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.gca().set_aspect('equal', adjustable='box')  # Mantém as proporções corretas
plt.grid(True, linestyle=':', alpha=0.6)

# Títulos e legendas
plt.title('Gráfico de uma Elipse', fontsize=14)
plt.xlabel('Eixo X', fontsize=12)
plt.ylabel('Eixo Y', fontsize=12)
plt.legend(loc='upper right')

# Exibe o gráfico
plt.show()