import numpy as np
import matplotlib.pyplot as plt

# 1. Criar a grade de pontos (X, Y) no plano cartesiano
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# 2. Definir as componentes do vetor para um campo convergente
# Para convergir para a origem, as componentes devem ser proporcionais a -X e -Y
U = -X
V = -Y

# Opcional: Normalizar os vetores para que todos tenham o mesmo comprimento 
# (deixando a visualização da direção mais limpa)
magnitude = np.sqrt(U**2 + V**2)
# Evita divisão por zero no centro
magnitude[magnitude == 0] = 1 
U_norm = U / magnitude
V_norm = V / magnitude

# 3. Plotar o campo vetorial
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, U_norm, V_norm, magnitude, cmap='Blues', pivot='mid', scale=25)