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

# 2. Gráfico de Barras (Comparação de Categoria)
categorias = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
vendas = [120, 85, 140, 95]

plt.figure(figsize=(8, 4))
plt.bar(categorias, vendas, color='skyblue', edgecolor='navy')
plt.title('Vendas por Categoria')
plt.xlabel('Categorias')
plt.ylabel('Unidades Vendidas')
plt.tight_layout()
plt.show()

# 3. Gráfico de Dispersão (Scatter Plot)
np.random.seed(42)
dados_x = np.random.randn(50)
dados_y = np.random.randn(50)