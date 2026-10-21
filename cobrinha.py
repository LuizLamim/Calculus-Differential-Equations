import sys
import random
import pygame

# Inicialização do Pygame
pygame.init()

# Configurações da Tela
LARGURA = 600
ALTURA = 400
TAMANHO_BLOCO = 20
VELOCIDADE = 10

# Cores (RGB)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()

def gerar_comida():
    x = random.randint(0, (LARGURA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    y = random.randint(0, (ALTURA - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    return [x, y]

def jogo():
    # Posição inicial da cobrinha
    cobra = [[200, 200], [180, 200], [160, 200]]
    direcao = "DIREITA"

    comida = gerar_comida()
    pontos = 0