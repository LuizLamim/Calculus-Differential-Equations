from manim import *
import numpy as np

# Configuração para formato vertical (9:16)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class PropriedadeFocal(Scene):
    def construct(self):
        # Fundo preto é o padrão do Manim
        
        # Parâmetros da elipse vertical
        a = 3 # semi-eixo menor (horizontal)
        b = 5 # semi-eixo maior (vertical)
        c = np.sqrt(b**2 - a**2) # Distância focal = 4
        
        F1_pos = np.array([0, -c, 0])
        F2_pos = np.array([0, c, 0])
        
        # Desenhar Elipse e Focos
        elipse = Ellipse(width=2*a, height=2*b, color=BLUE)
        foco1 = Dot(F1_pos, color=YELLOW)
        foco2 = Dot(F2_pos, color=YELLOW)
        
        f1_label = MathTex("F_1").next_to(foco1, DOWN)
        f2_label = MathTex("F_2").next_to(foco2, UP)
        
        self.play(Create(elipse), FadeIn(foco1, foco2, f1_label, f2_label))
        self.wait(1)
        
        # Gerar 10 ângulos para as trajetórias
        angles = np.linspace(0, 2*np.pi, 10, endpoint=False)
        
        bolas = VGroup()
        rastros = VGroup()
        animacoes = []
        
        # Velocidade constante para todas as bolas
        velocidade = 4.0