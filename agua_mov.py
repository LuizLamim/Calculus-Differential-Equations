import pygame
import math
import random

# Configurações gerais
LARGURA = 800
ALTURA = 600
FPS = 60

# Configurações das Partículas
NUM_PARTICULAS = 250
RAIO_PARTICULA = 8
RAIO_INTERACAO = 35     # Distância máxima de repulsão entre partículas
FORCA_REPULSAO = 0.8    # Intensidade da repulsão do fluido
GRAVIDADE = 0.35        # Força da gravidade puxando para baixo
AMORTECIMENTO = 0.85    # Perda de energia ao colidir com as paredes