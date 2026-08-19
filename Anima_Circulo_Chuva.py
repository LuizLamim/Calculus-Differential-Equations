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

# Classe que define cada círculo da chuva
class Circulo:
    def __init__(self):
        # Tamanho aleatório
        self.raio = random.randint(3, 15)
        # Posição X aleatória ao longo da tela
        self.x = random.randint(0, LARGURA)
        # Começa acima da tela para um início suave
        self.y = random.randint(-ALTURA, 0)
        # Velocidade de queda baseada no tamanho (maiores caem mais rápido)
        self.velocidade = self.raio * 0.5 + random.uniform(1, 3)
        # Cores em tons de azul/ciano para simular água/chuva
        self.cor = (
            random.randint(50, 100),   # Red
            random.randint(150, 255),  # Green
            random.randint(200, 255)   # Blue
        )

    def cair(self):
        # Move o círculo para baixo
        self.y += self.velocidade
        
        # Se o círculo passar do fundo da tela, ele ressurge no topo
        if self.y - self.raio > ALTURA:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, LARGURA)
            self.velocidade = self.raio * 0.5 + random.uniform(1, 3)

    def desenhar(self, superficie):
        pygame.draw.circle(superficie, self.cor, (int(self.x), int(self.y)), self.raio)

# Cria uma lista contendo 150 círculos
quantidade_circulos = 150
circulos = [Circulo() for _ in range(quantidade_circulos)]

# Relógio para controlar os Frames por Segundo (FPS)
relogio = pygame.time.Clock()
rodando = True

# Loop principal da animação
while rodando:
    # Checa eventos (como fechar a janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Preenche o fundo de preto a cada frame para apagar o frame anterior
    tela.fill(PRETO)

    # Atualiza a posição e desenha cada círculo
    for circulo in circulos:
        circulo.cair()
        circulo.desenhar(tela)

    # Atualiza a tela
    pygame.display.flip()
    
    # Limita a animação a 60 FPS
    relogio.tick(60)

# Encerra o Pygame
pygame.quit()