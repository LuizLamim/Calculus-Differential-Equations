import matplotlib.pyplot as plt
import numpy as np

# Configuração visual do Matplotlib
plt.style.use('seaborn-v0_8-whitegrid')

# 1. Gráfico de Linha (Função Seno)
x = np.linspace(0, 10, 100)
y = np.sin(x)