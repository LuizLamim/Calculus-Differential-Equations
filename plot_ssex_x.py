import matplotlib.pyplot as plt
import numpy as np

# Definindo o intervalo de x (ex: de -2π a 2π)
x = np.linspace(-2 * np.pi, 2 * np.pi, 2000)

# Calculando a secante e aplicando o valor absoluto |sec(x)|
y = np.abs(1 / np.cos(x))

# Removendo descontinuidades (assíntotas) para não desenhar linhas verticais falsas
y[y > 10] = np.nan