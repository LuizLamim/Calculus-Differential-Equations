import numpy as np
import matplotlib.pyplot as plt

def simular_navier_stokes():
    # 1. Configuração da Grade de Simulação
    nx, ny = 41, 41           # Número de pontos na grade (X, Y)
    lx, ly = 2.0, 2.0         # Dimensões do domínio
    dx = lx / (nx - 1)
    dy = ly / (ny - 1)
    
    # Parâmetros físicos e de tempo
    nt = 100                  # Número de passos de tempo
    dt = 0.001                # Intervalo de tempo (Δt)
    rho = 1.0                 # Densidade do fluido (ρ)
    nu = 0.1                  # Viscosidade cinemática (ν)
    nit = 50                  # Iterações para resolver a equação de Poisson da pressão

    # Matrizes de velocidade e pressão
    u = np.zeros((ny, nx))    # Velocidade na direção X
    v = np.zeros((ny, nx))    # Velocidade na direção Y
    p = np.zeros((ny, nx))    # Pressão
    b = np.zeros((ny, nx))    # Termo fonte da pressão

    # Condição Inicial: Criação de um Vórtice no centro do domínio
    x = np.linspace(0, lx, nx)
    y = np.linspace(0, ly, ny)
    X, Y = np.meshgrid(x, y)
    
    # Perfil de velocidade circular ao redor do ponto (1.0, 1.0)
    r_sq = (X - 1.0)**2 + (Y - 1.0)**2
    u = -np.sin(np.pi * (Y - 1.0)) * np.exp(-r_sq * 5)
    v =  np.sin(np.pi * (X - 1.0)) * np.exp(-r_sq * 5)

    # 2. Resolução do Termo Fonte da Pressão
    def construir_termo_b(b, rho, dt, u, v, dx, dy):
        b[1:-1, 1:-1] = (rho * (1 / dt * 
                        ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx) + 
                         (v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy)) -
                        ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx))**2 -
                        2 * ((u[2:, 1:-1] - u[0:-2, 1:-1]) / (2 * dy) *
                             (v[1:-1, 2:] - v[1:-1, 0:-2]) / (2 * dx)) -
                        ((v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy))**2))
        return b