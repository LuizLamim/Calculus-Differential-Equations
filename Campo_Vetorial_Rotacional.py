import numpy as np
import matplotlib.pyplot as plt

# 1. Definindo o espaço (grid)
x = np.linspace(-5, 5, 20) # Cria 20 pontos de -5 a 5 no eixo X
y = np.linspace(-5, 5, 20) # Cria 20 pontos de -5 a 5 no eixo Y
X, Y = np.meshgrid(x, y)   # Cria uma malha 2D com esses pontos

# 2. Definindo as componentes do campo vetorial rotacional
# V(x, y) = -y*i + x*j
U = -Y  # Componente X do vetor
V = X   # Componente Y do vetor

# 3. Calculando a magnitude (tamanho) dos vetores para colorí-los
# np.hypot calcula a hipotenusa (sqrt(U**2 + V**2))
M = np.hypot(U, V)

# 4. Configurando e plotando o gráfico
plt.figure(figsize=(8, 8))

# A função quiver é a responsável por desenhar o campo de vetores (setas)
# Passamos X, Y (posições), U, V (direções) e M (cores baseadas na magnitude)
plt.quiver(X, Y, U, V, M, cmap='viridis', pivot='mid')

# Adicionando detalhes ao gráfico
plt.title('Campo Vetorial Rotacional\n$\mathbf{V}(x,y) = -y\hat{i} + x\hat{j}$')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True, linestyle='--', alpha=0.6)