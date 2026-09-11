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

# Formatação dos rótulos do eixo X em múltiplos de π/2
xticks = np.arange(-2 * np.pi, 2.5 * np.pi, np.pi / 2)
xtick_labels = [
    r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$',
    '0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'
]
plt.xticks(xticks, xtick_labels)