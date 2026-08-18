import matplotlib.pyplot as plt
import numpy as np

# 1. Definir a grade de pontos (x, y)
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# 2. Definir a função escalar f(x, y)
# Exemplo: f(x, y) = x^2 + y^2
Z = X**2 + Y**2

# 3. Calcular o Vetor Gradiente (df/dx, df/dy)
# O gradiente analítico de x^2 + y^2 é (2x, 2y)
# Também podemos usar np.gradient para calcular numericamente:
U, V = np.gradient(Z, x[1] - x[0], y[1] - y[0])

# 4. Configurar a figura
fig, ax = plt.subplots(figsize=(8, 7))