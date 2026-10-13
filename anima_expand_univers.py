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