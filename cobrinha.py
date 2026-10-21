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

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != "BAIXO":
                    direcao = "CIMA"
                elif evento.key == pygame.K_DOWN and direcao != "CIMA":
                    direcao = "BAIXO"
                elif evento.key == pygame.K_LEFT and direcao != "DIREITA":
                    direcao = "ESQUERDA"
                elif evento.key == pygame.K_RIGHT and direcao != "ESQUERDA":
                    direcao = "DIREITA"

        # Atualiza a posição da cabeça
        cabeca_x, cabeca_y = cobra[0]
        if direcao == "CIMA":
            cabeca_y -= TAMANHO_BLOCO
        elif direcao == "BAIXO":
            cabeca_y += TAMANHO_BLOCO
        elif direcao == "ESQUERDA":
            cabeca_x -= TAMANHO_BLOCO
        elif direcao == "DIREITA":
            cabeca_x += TAMANHO_BLOCO

        nova_cabeca = [cabeca_x, cabeca_y]

        # Colisão com as paredes
        if (
            cabeca_x < 0
            or cabeca_x >= LARGURA
            or cabeca_y < 0
            or cabeca_y >= ALTURA
        ):
            rodando = False

        # Colisão com o próprio corpo
        if nova_cabeca in cobra:
            rodando = False

        cobra.insert(0, nova_cabeca)

        # Checa se comeu a comida
        if nova_cabeca == comida:
            pontos += 1
            comida = gerar_comida()
        else:
            cobra.pop()  # Remove a cauda se não comeu

        # Desenho na tela
        tela.fill(PRETO)

        # Desenha a comida (Vermelha)
        pygame.draw.rect(
            tela, VERMELHO, (comida[0], comida[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
        )

        # Desenha a cobrinha (Verde)
        for parte in cobra:
            pygame.draw.rect(
                tela, VERDE, (parte[0], parte[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
            )

        # Exibe pontuação
        fonte = pygame.font.SysFont(None, 30)
        texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
        tela.blit(texto, (10, 10))

        pygame.display.flip()
        relogio.tick(VELOCIDADE)

    # Mensagem de Game Over
    tela.fill(PRETO)
    fonte = pygame.font.SysFont(None, 50)
    texto_game_over = fonte.render("GAME OVER", True, VERMELHO)
    texto_pontos = fonte.render(f"Pontuação Final: {pontos}", True, BRANCO)
    tela.blit(texto_game_over, (LARGURA // 4, ALTURA // 3))
    tela.blit(texto_pontos, (LARGURA // 5, ALTURA // 2))
    pygame.display.flip()
    pygame.time.wait(2000)


if __name__ == "__main__":
    jogo()