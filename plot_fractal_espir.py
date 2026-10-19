import numpy as np
import matplotlib.pyplot as plt

def gerar_espiral_fractal(num_pontos=100000):
    """
    Gera as coordenadas (x, y) de um fractal em espiral 
    usando um Sistema de Funções Iteradas (IFS).
    """
    x = np.zeros(num_pontos)
    y = np.zeros(num_pontos)

    # Matrizes de transformação e vetores de translação
    # Cada linha representa uma transformação contendo: [a, b, c, d, e, f, probabilidade]
    # onde:
    # x_novo = a*x + b*y + e
    # y_novo = c*x + d*y + f
    transformacoes = [
        # Contrair e rotacionar para formar a espiral principal
        [0.97 * np.cos(0.165), -0.97 * np.sin(0.165), 0.97 * np.sin(0.165), 0.97 * np.cos(0.165), 0.0, 1.0, 0.90],
        # Ramificação interna 1
        [0.40 * np.cos(1.2),   -0.40 * np.sin(1.2),   0.40 * np.sin(1.2),   0.40 * np.cos(1.2),   0.0, 0.5, 0.05],
        # Ramificação interna 2
        [0.40 * np.cos(-1.2),  -0.40 * np.sin(-1.2),  0.40 * np.sin(-1.2),  0.40 * np.cos(-1.2),  0.0, 0.5, 0.05]
    ]

    probabilidades = [t[6] for t in transformacoes]
    
    # Sorteia qual transformação aplicar a cada passo
    escolhas = np.random.choice(len(transformacoes), size=num_pontos, p=probabilidades)

    # Iteração para gerar os pontos
    for i in range(1, num_pontos):
        t = transformacoes[escolhas[i]]
        x[i] = t[0] * x[i-1] + t[1] * y[i-1] + t[4]
        y[i] = t[2] * x[i-1] + t[3] * y[i-1] + t[5]

    return x, y

def plotar_fractal():
    x, y = gerar_espiral_fractal(num_pontos=200000)

    # Configuração da figura
    plt.figure(figsize=(10, 10), facecolor='black')
    ax = plt.subplot(111, facecolor='black')

    # Plotando os pontos com mapa de cores dinâmico baseado na distância do centro
    raio = np.sqrt(x**2 + y**2)
    plt.scatter(x, y, s=0.1, c=raio, cmap='magma', alpha=0.6)

    # Estilização
    plt.title("Fractal em Espiral", color='white', fontsize=16, pad=15)
    plt.axis('equal')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plotar_fractal()