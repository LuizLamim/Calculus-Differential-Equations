import matplotlib.pyplot as plt
import numpy as np

# 1. Criar a grade de pontos no plano 2D (x, y)
x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)

# 2. Definir a função escalar f(x, y)
# Exemplo: f(x, y) = x² + y² (um paraboloide)
Z = X**2 + Y**2

# 3. Calcular o gradiente numericamente: ∇f = (df/dx, df/dy)
# Nota: np.gradient retorna primeiro a variação no eixo vertical (y) e depois no horizontal (x)
dF_dy, dF_dx = np.gradient(Z, y[1] - y[0], x[1] - x[0])

# 4. Configurar a figura
plt.figure(figsize=(8, 6))