import numpy as np
import matplotlib.pyplot as plt

# 1. Criar a grade de pontos (X, Y) no plano cartesiano
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# 2. Definir as componentes do vetor para um campo convergente
# Para convergir para a origem, as componentes devem ser proporcionais a -X e -Y
U = -X
V = -Y