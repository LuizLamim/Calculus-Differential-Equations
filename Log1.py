import numpy as np
import matplotlib.pyplot as plt

# Gera valores de x maiores que 0 (já que o log não existe para x <= 0)
# Começamos de 0.1 até 10 com 400 pontos para a curva ficar suave
x = np.linspace(0.1, 10, 400)