import numpy as np
import matplotlib.pyplot as plt

# Define os intervalos para x evitando o zero (onde a função não é definida)
x_neg = np.linspace(-10, -0.1, 500)
x_pos = np.linspace(0.1, 10, 500)