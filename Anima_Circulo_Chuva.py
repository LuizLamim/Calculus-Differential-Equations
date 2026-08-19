import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da Tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Chuva de Círculos")

# Cores
PRETO = (0, 0, 0)