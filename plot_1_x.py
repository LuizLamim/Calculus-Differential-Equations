import numpy as np
import matplotlib.pyplot as plt

# Define os intervalos de x (separados para evitar x = 0)
x_negativos = np.linspace(-5, -0.02, 400)
x_positivos = np.linspace(0.02, 5, 400)

# Calcula f(x) = |1/x| para ambos os lados
y_negativos = np.abs(1 / x_negativos)
y_positivos = np.abs(1 / x_positivos)

# Configura a figura do gráfico
plt.figure(figsize=(8, 6))

# Plota os dois lados da função
plt.plot(x_negativos, y_negativos, color='blue', label=r'$f(x) = \left|\frac{1}{x}\right|$')
plt.plot(x_positivos, y_positivos, color='blue')

# Configura os eixos cartesianos no centro (0,0)
plt.axhline(0, color='black', linewidth=1.2) # Eixo X
plt.axvline(0, color='black', linewidth=1.2) # Eixo Y

# Limita os eixos para melhor visualização (foca na curva principal)
plt.xlim(-5, 5)
plt.ylim(-1, 20)