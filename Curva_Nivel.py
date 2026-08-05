import matplotlib.pyplot as plt
import numpy as np

# 1. Definir o domínio de X e Y
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)

# 2. Criar a grade bidimensional (Meshgrid)
X, Y = np.meshgrid(x, y)

# 3. Definir a função z = f(x, y)
# Exemplo: z = sin(sqrt(x^2 + y^2))
Z = np.sin(np.sqrt(X**2 + Y**2))