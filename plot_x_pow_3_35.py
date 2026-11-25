import matplotlib.pyplot as plt
import numpy as np

# 1. Define o intervalo de valores para x (de -10 a 10, com 400 pontos)
x = np.linspace(-10, 10, 400)

# 2. Calcula os valores de y segundo a função f(x) = x^3 + 35
y = x**3 + 35

# 3. Cria a figura e plota a curva
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$f(x) = x^3 + 35$", color="#1f77b4", linewidth=2)