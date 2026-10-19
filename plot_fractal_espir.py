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