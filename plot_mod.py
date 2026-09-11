import matplotlib.pyplot as plt
import numpy as np

# Configuração do domínio x de -2π a 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Cálculo do módulo das funções trigonométricas
y_cos = np.abs(np.cos(x))
y_sin = np.abs(np.sin(x))

# Criação da figura
plt.figure(figsize=(10, 5))

# Plotagem das curvas
plt.plot(x, y_cos, label=r'$|\cos(x)|$', color='crimson', linewidth=2)
plt.plot(x, y_sin, label=r'$|\sin(x)|$', color='dodgerblue', linewidth=2)