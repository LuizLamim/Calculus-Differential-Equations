import numpy as np
import matplotlib.pyplot as plt

# Define os intervalos de x (separados para evitar x = 0)
x_negativos = np.linspace(-5, -0.02, 400)
x_positivos = np.linspace(0.02, 5, 400)

# Calcula f(x) = |1/x| para ambos os lados
y_negativos = np.abs(1 / x_negativos)
y_positivos = np.abs(1 / x_positivos)