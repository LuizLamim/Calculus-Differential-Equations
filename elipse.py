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
        
        for theta in angles:
            # Ponto na elipse onde a bola vai bater
            # Como a elipse é vertical, x = a*cos(theta), y = b*sin(theta)
            P = np.array([a * np.cos(theta), b * np.sin(theta), 0])
            
            # Distâncias D1 (F1 -> P) e D2 (P -> F2)
            d1 = np.linalg.norm(P - F1_pos)
            d2 = np.linalg.norm(P - F2_pos)
            
            # Criar bola
            bola = Dot(F1_pos, color=RED, radius=0.08)
            bolas.add(bola)
            
            # Criar rastro (trail)
            rastro = TracedPath(bola.get_center, stroke_width=2, stroke_color=WHITE, stroke_opacity=0.6)
            rastros.add(rastro)
            
            # Tempos de viagem (t = d / v)
            t1 = d1 / velocidade
            t2 = d2 / velocidade
            
            # Animações de movimento
            # O Succession cria a sequência: vai de F1 para P, depois reflete de P para F2
            movimento1 = bola.animate(run_time=t1, rate_func=linear).move_to(P)
            movimento2 = bola.animate(run_time=t2, rate_func=linear).move_to(F2_pos)
            
            animacoes.append(Succession(movimento1, movimento2))

        # Adicionar os rastros à cena antes de animar
        self.add(rastros)
        
        # Tocar todas as animações simultaneamente
        # Como D1 + D2 = constante (2b) para qualquer ponto da elipse,
        # todas as bolas chegarão em F2 exatamente no mesmo instante!
        self.play(*animacoes)
        self.wait(2)