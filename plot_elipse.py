import matplotlib.pyplot as plt
import numpy as np

# Parâmetros da elipse
h, k = 0, 0  # Centro da elipse (h, k)
a = 5        # Semieixo maior (horizontal)
b = 3        # Semieixo menor (vertical)

# Ângulo t variando de 0 a 2π
t = np.linspace(0, 2 * np.pi, 500)

# Equações paramétricas da elipse
x = h + a * np.cos(t)
y = k + b * np.sin(t)

# Configuração do gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'Elipse: a={a}, b={b}', color='blue', linewidth=2)
plt.plot(h, k, 'ro', label='Centro (0,0)')  # Plota o ponto do centro