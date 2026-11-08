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

# Matriz de rotação total (a ordem das multiplicações importa)
R_total = R_Omega @ R_i @ R_omega

# 3. Aplicando a rotação tridimensional às coordenadas orbitais
x, y, z = R_total @ coords

# 4. Configurando a visualização do gráfico 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotando a órbita de Plutão
ax.plot(x, y, z, color='purple', linewidth=2, label='Órbita de Plutão')

# Plotando o Sol na origem (foco geométrico)
ax.scatter(0, 0, 0, color='yellow', s=200, edgecolor='orange', label='Sol')

# Plotando o plano da Eclíptica (órbita da Terra como referência) para mostrar a inclinação
# Um círculo simples no plano Z=0 com raio de 39 UA para comparação de escala
theta = np.linspace(0, 2*np.pi, 100)
ax.plot(39.48 * np.cos(theta), 39.48 * np.sin(theta), 0, color='gray', linestyle='--', alpha=0.5, label='Plano da Eclíptica de referência')

# Configurações visuais do gráfico
ax.set_title("Órbita 3D de Plutão", fontsize=14, fontweight='bold')
ax.set_xlabel("Eixo X (UA)")
ax.set_ylabel("Eixo Y (UA)")
ax.set_zlabel("Eixo Z (UA)")

# Forçando o aspecto cúbico para evitar distorções na excentricidade da elipse
limite = 45
ax.set_xlim([-limite, limite])
ax.set_ylim([-limite, limite])
ax.set_zlim([-limite, limite])

# Fundo escuro para visualização espacial (Opcional)
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.zaxis.label.set_color('white')
ax.title.set_color('white')
ax.tick_params(colors='white')
ax.grid(False)

# Adicionando legenda
ax.legend(facecolor='black', labelcolor='white')

# Exibir gráfico
plt.show()