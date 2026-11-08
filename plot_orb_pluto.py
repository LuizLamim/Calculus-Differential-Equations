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