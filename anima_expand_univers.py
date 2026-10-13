import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configurações iniciais da simulação
num_galaxies = 150
num_frames = 150

# Geração de posições iniciais das galáxias em um disco (distribuição aleatória)
np.random.seed(42)
r = np.random.uniform(1.0, 10.0, num_galaxies)
theta = np.random.uniform(0, 2 * np.pi, num_galaxies)

x0 = r * np.cos(theta)
y0 = r * np.sin(theta)

# Configuração da figura e dos eixos (fundo preto simulando o espaço profundo)
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
fig.patch.set_facecolor('black')

# Gráfico de dispersão (scatter plot) para as galáxias
scat = ax.scatter([], [], c=[], cmap='cool', s=50, edgecolors='none', alpha=0.8)

# Limites dos eixos espaciais
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.axis('off')  # O espaço não tem bordas visíveis

# Título dinâmico da animação
title = ax.text(0, 31, '', color='white', fontsize=14, ha='center', fontweight='bold')

def init():
    """Inicializa a animação."""
    scat.set_offsets(np.empty((0, 2)))
    title.set_text('')
    return scat, title

def animate(i):
    """Atualiza a posição das galáxias a cada quadro (frame)."""
    # Fator de escala do universo a(t) acelerando com o tempo (simulando energia escura)
    a_t = 1.0 + (i / 30) ** 1.3
    
    # As posições expandem proporcionalmente ao fator de escala
    x = x0 * a_t
    y = y0 * a_t
    
    # Atualiza as coordenadas das galáxias
    data = np.stack([x, y], axis=-1)
    scat.set_offsets(data)
    
    # Mapeia cores baseadas na distância para dar um efeito visual dinâmico
    distances = np.sqrt(x**2 + y**2)
    scat.set_array(distances)
    
    # Atualiza o texto informativo na tela
    title.set_text(f'Expansão do Universo | Fator de Escala a(t): {a_t:.2f}')
    return scat, title

# Criação da animação
ani = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=num_frames, interval=40, blit=True
)

# Exibe a animação interativa
plt.tight_layout()
plt.show()

# Opcional: Para salvar a animação como GIF (descomente a linha abaixo se tiver o pillow instalado)
# ani.save('expansao_universo.gif', writer='pillow', fps=30)