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

class Particula:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def atualizar(self):
        # Aplica a gravidade
        self.vy += GRAVIDADE

        # Atualiza a posição
        self.x += self.vx
        self.y += self.vy

        # Colisão com as paredes da janela
        if self.x - RAIO_PARTICULA < 0:
            self.x = RAIO_PARTICULA
            self.vx *= -AMORTECIMENTO
        elif self.x + RAIO_PARTICULA > LARGURA:
            self.x = LARGURA - RAIO_PARTICULA
            self.vx *= -AMORTECIMENTO

        if self.y - RAIO_PARTICULA < 0:
            self.y = RAIO_PARTICULA
            self.vy *= -AMORTECIMENTO
        elif self.y + RAIO_PARTICULA > ALTURA:
            self.y = ALTURA - RAIO_PARTICULA
            self.vy *= -AMORTECIMENTO

    def desenhar(self, tela):
        # Modifica o tom de azul de acordo com a velocidade para um efeito dinâmico
        velocidade = math.hypot(self.vx, self.vy)
        azul = min(255, int(150 + velocidade * 15))
        cor = (30, 144, azul)
        
        pygame.draw.circle(tela, cor, (int(self.x), int(self.y)), RAIO_PARTICULA)