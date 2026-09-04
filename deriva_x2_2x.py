import matplotlib.pyplot as plt
import numpy as np

# 1. Gerando os valores de x (de -10 até 10 com 400 pontos para suavizar a curva)
x = np.linspace(-10, 10, 400)

# 2. Definindo as funções
y_quadratica = x**2
y_linear = 2 * x

# 3. Configurando a figura do gráfico
plt.figure(figsize=(8, 6))

# Plotando as duas funções
plt.plot(x, y_quadratica, label="y = x²", color="blue", linewidth=2)
plt.plot(x, y_linear, label="y = 2x", color="red", linewidth=2)

# 4. Adicionando personalizações para melhorar a visualização
plt.title("Gráfico das funções y = x² e y = 2x", fontsize=14)
plt.xlabel("Eixo X", fontsize=12)
plt.ylabel("Eixo Y", fontsize=12)