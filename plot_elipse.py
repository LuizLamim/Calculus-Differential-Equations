import matplotlib.pyplot as plt
import numpy as np

# Parâmetros da elipse
h, k = 0, 0  # Centro da elipse (h, k)
a = 5        # Semieixo maior (horizontal)
b = 3        # Semieixo menor (vertical)

# Ângulo t variando de 0 a 2π
t = np.linspace(0, 2 * np.pi, 500)

# Equações paramétricas da elipse
x = h + a * np.cos(t)
y = k + b * np.sin(t)