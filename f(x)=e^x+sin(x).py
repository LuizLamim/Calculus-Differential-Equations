import numpy as np
import matplotlib.pyplot as plt

# 1. Define o intervalo de valores para x (de -3 a 3 com 500 pontos)
x = np.linspace(-3, 3, 500)

# 2. Calcula os valores da função f(x) = e^x + sin(x)
y = np.exp(x) + np.sin(x)

# 3. Configura o gráfico
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x) = e^x + \sin(x)$', color='purple', linewidth=2)