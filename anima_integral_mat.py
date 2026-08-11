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

# Função de inicialização da animação
def init():
    ax.clear()
    ax.set_xlim(a - 0.2, b + 0.2)
    ax.set_ylim(0, max(y_curve) + 1)
    ax.set_title("Introdução ao Cálculo Integral: Soma de Riemann", fontsize=14, fontweight='bold')
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True, linestyle="--", alpha=0.5)
    
    # Desenha a curva principal
    ax.plot(x_curve, y_curve, color="blue", linewidth=2.5, label=r"$f(x) = x^2 + 1$")
    ax.legend(loc="upper left")
    return ax,

# 3. Função de atualização (executada em cada quadro/frame da animação)
def update(frame):
    # O número de retângulos (n) cresce a cada quadro
    # frame vai de 0 a 30, então n vai de 1 até 31
    n = frame + 1
    
    # Limpa as barras anteriores mantendo os eixos configurados
    init()
    
    # Largura de cada retângulo (dx)
    dx = (b - a) / n
    
    # Pontos à esquerda de cada subintervalo (Soma de Riemann à esquerda)
    x_left = np.linspace(a, b - dx, n)
    y_left = f(x_left)
    
    # Área aproximada atual
    area_approx = np.sum(y_left * dx)
    
    # Área exata via Integral Definitiva: ∫(x^2 + 1) dx de 0 a 2 = [x^3/3 + x] = 8/3 + 2 = 14/3 ≈ 4.6667
    area_exact = 14 / 3 
    
    # Desenha os retângulos de aproximação
    bars = ax.bar(
        x_left, 
        y_left, 
        width=dx, 
        align='edge', 
        color='orange', 
        edgecolor='darkred', 
        alpha=0.5,
        label=f"Retângulos (n = {n})"
    )
    
    # Texto explicativo no gráfico
    text_info = (
        f"Número de retângulos (n): {n}\n"
        f"Largura (Δx): {dx:.4f}\n"
        f"Área aproximada: {area_approx:.4f}\n"
        f"Área exata (Integral): {area_exact:.4f}"
    )
    
    ax.text(
        0.05, 0.65, text_info, 
        transform=ax.transAxes, 
        fontsize=11, 
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
    )
    
    ax.legend(loc="upper left")
    return ax,

# 4. Criando a animação
# frames: número de quadros (n varia de 1 a 35 retângulos)
# interval: tempo entre quadros em milissegundos
ani = FuncAnimation(fig, update, frames=35, init_func=init, interval=400, repeat=True)

# Exibe a animação na tela
plt.show()