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