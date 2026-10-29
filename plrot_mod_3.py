import numpy as np
import matplotlib.pyplot as plt

# Define o intervalo de valores para x (de -10 a 10, com 400 pontos para uma curva suave)
x = np.linspace(-10, 10, 400)

# Define a função y = |x| + 3
y = np.abs(x) + 3