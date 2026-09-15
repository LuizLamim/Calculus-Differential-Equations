import numpy as np
import matplotlib.pyplot as plt

# Define os intervalos para x evitando o zero (onde a função não é definida)
x_neg = np.linspace(-10, -0.1, 500)
x_pos = np.linspace(0.1, 10, 500)

# Calcula os valores correspondentes de y
y_neg = 1 / x_neg
y_pos = 1 / x_pos

# Configura a figura
plt.figure(figsize=(8, 6))

# Plota as duas curvas
plt.plot(x_neg, y_neg, color='blue', linewidth=2, label=r'$f(x) = \frac{1}{x}$')
plt.plot(x_pos, y_pos, color='blue', linewidth=2)

# Adiciona as assíntotas (eixos x = 0 e y = 0)
plt.axhline(0, color='black', linestyle='--', alpha=0.7)
plt.axvline(0, color='black', linestyle='--', alpha=0.7)