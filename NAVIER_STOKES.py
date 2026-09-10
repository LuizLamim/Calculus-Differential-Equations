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

    # 3. Solver da Equação de Poisson para a Pressão
    def poisson_pressao(p, dx, dy, b):
        pn = np.empty_like(p)
        for _ in range(nit):
            pn = p.copy()
            p[1:-1, 1:-1] = (((pn[1:-1, 2:] + pn[1:-1, 0:-2]) * dy**2 +
                              (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx**2) /
                             (2 * (dx**2 + dy**2)) -
                             dx**2 * dy**2 / (2 * (dx**2 + dy**2)) * b[1:-1, 1:-1])

            # Condições de contorno para pressão (Dirichlet/Neumann)
            p[:, -1] = p[:, -2]  # dp/dx = 0 em x = 2
            p[0, :] = p[1, :]    # dp/dy = 0 em y = 0
            p[:, 0] = p[:, 1]    # dp/dx = 0 em x = 0
            p[-1, :] = 0         # p = 0 em y = 2
        return p

    # 4. Loop Principal de Avanço no Tempo
    for n in range(nt):
        un = u.copy()
        vn = v.copy()
        
        b = construir_termo_b(b, rho, dt, u, v, dx, dy)
        p = poisson_pressao(p, dx, dy, b)
        
        # Atualização das velocidades (Advecção + Gradiente de Pressão + Difusão Viscosa)
        u[1:-1, 1:-1] = (un[1:-1, 1:-1] -
                         un[1:-1, 1:-1] * dt / dx * (un[1:-1, 1:-1] - un[1:-1, 0:-2]) -
                         vn[1:-1, 1:-1] * dt / dy * (un[1:-1, 1:-1] - un[0:-2, 1:-1]) -
                         dt / (2 * rho * dx) * (p[1:-1, 2:] - p[1:-1, 0:-2]) +
                         nu * (dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                               dt / dy**2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])))

        v[1:-1, 1:-1] = (vn[1:-1, 1:-1] -
                         un[1:-1, 1:-1] * dt / dx * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) -
                         vn[1:-1, 1:-1] * dt / dy * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) -
                         dt / (2 * rho * dy) * (p[2:, 1:-1] - p[0:-2, 1:-1]) +
                         nu * (dt / dx**2 * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) +
                               dt / dy**2 * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1])))
        
        # Condições de contorno para velocidade (paredes sem escorregamento)
        u[0, :] = 0
        u[-1, :] = 0
        u[:, 0] = 0
        u[:, -1] = 0
        v[0, :] = 0
        v[-1, :] = 0
        v[:, 0] = 0
        v[:, -1] = 0

    # 5. Plotagem dos Resultados
    magnitude_velocidade = np.sqrt(u**2 + v**2)
    
    plt.figure(figsize=(8, 6), dpi=100)
    
    # Campo de magnitudes (fundo colorido)
    plt.contourf(X, Y, magnitude_velocidade, alpha=0.8, cmap='viridis')
    plt.colorbar(label='Magnitude da Velocidade')
    
    # Linhas de corrente com vetores
    plt.streamplot(X, Y, u, v, color='white', density=1.2, linewidth=1)
    
    plt.title('Campo de Velocidade - Navier-Stokes 2D (Vórtice)')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.xlim(0, lx)
    plt.ylim(0, ly)
    plt.show()

# Executa o programa
if __name__ == '__main__':
    simular_navier_stokes()