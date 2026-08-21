import numpy as np
import matplotlib.pyplot as plt

# 1. Define o intervalo de valores para o eixo x (de -3 a 3 com 400 pontos)
x = np.linspace(-3, 3, 400)

# 2. Calcula a função f(x) = |e^x|
# np.exp(x) calcula e^x, e np.abs() aplica o valor absoluto
y = np.abs(np.exp(x))

# 3. Cria a figura e define o tamanho
plt.figure(figsize=(8, 6))

# 4. Plota o gráfico com uma linha azul
plt.plot(x, y, color='blue', linewidth=2, label=r'$f(x) = |e^x|$')

# 5. Adiciona títulos e rótulos
plt.title('Gráfico da Função $f(x) = |e^x|$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)

# 6. Destaca os eixos centrais (x=0 e y=0)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# 7. Adiciona uma grade de fundo e a legenda
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# 8. Exibe o gráfico na tela
plt.show()