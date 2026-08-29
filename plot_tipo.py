import matplotlib.pyplot as plt
import numpy as np

# Configuração visual do Matplotlib
plt.style.use('seaborn-v0_8-whitegrid')

# 1. Gráfico de Linha (Função Seno)
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color='blue', linewidth=2, label='sen(x)')
plt.title('Gráfico de Linha - Função Seno')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.tight_layout()
plt.show()