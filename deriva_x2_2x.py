import matplotlib.pyplot as plt
import numpy as np

# 1. Gerando os valores de x (de -10 até 10 com 400 pontos para suavizar a curva)
x = np.linspace(-10, 10, 400)

# 2. Definindo as funções
y_quadratica = x**2
y_linear = 2 * x

# 3. Configurando a figura do gráfico
plt.figure(figsize=(8, 6))