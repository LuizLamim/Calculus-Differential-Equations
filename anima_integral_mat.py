import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Definição da função e do intervalo
def f(x):
    # Função para o exemplo: f(x) = x^2 + 1
    return x**2 + 1

a, b = 0, 2  # Intervalo [a, b]

# 2. Configuração da figura e dos eixos
fig, ax = plt.subplots(figsize=(9, 6))

# Pontos contínuos para desenhar a curva suave
x_curve = np.linspace(a - 0.2, b + 0.2, 400)
y_curve = f(x_curve)