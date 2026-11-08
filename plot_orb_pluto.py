import numpy as np
import matplotlib.pyplot as plt

# Parâmetros orbitais aproximados de Plutão
a = 39.48       # Semieixo maior em UA (Unidades Astronômicas)
e = 0.2488      # Excentricidade
i_deg = 17.16   # Inclinação em graus
omega_deg = 113.8 # Argumento do periélio em graus
Omega_deg = 110.3 # Longitude do nó ascendente em graus

# Convertendo graus para radianos
i = np.radians(i_deg)
omega = np.radians(omega_deg)
Omega = np.radians(Omega_deg)

# Anomalia excêntrica (E) gerando 1000 pontos de 0 a 2*pi
E = np.linspace(0, 2 * np.pi, 1000)

# 1. Coordenadas no plano orbital 2D da própria órbita (x', y')
x_prime = a * (np.cos(E) - e)
y_prime = a * np.sqrt(1 - e**2) * np.sin(E)
z_prime = np.zeros_like(x_prime)

# Empilhando as coordenadas para facilitar a multiplicação de matrizes
coords = np.vstack((x_prime, y_prime, z_prime))

# 2. Matrizes de rotação para converter para o referencial heliocêntrico (eclíptica)
# Rotação 1: Argumento do periélio (rotação ao redor do eixo Z)
R_omega = np.array([
    [np.cos(omega), -np.sin(omega), 0],
    [np.sin(omega),  np.cos(omega), 0],
    [0,             0,             1]
])

# Rotação 2: Inclinação orbital (rotação ao redor do eixo X)
R_i = np.array([
    [1, 0,          0],
    [0, np.cos(i), -np.sin(i)],
    [0, np.sin(i),  np.cos(i)]
])

# Rotação 3: Longitude do nó ascendente (rotação ao redor do eixo Z)
R_Omega = np.array([
    [np.cos(Omega), -np.sin(Omega), 0],
    [np.sin(Omega),  np.cos(Omega), 0],
    [0,             0,             1]
])