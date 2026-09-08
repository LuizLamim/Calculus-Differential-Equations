from manim import *

# Vídeo vertical 9:16 com fundo preto
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = BLACK
config.frame_rate = 30


class PropriedadeFocalElipse(Scene):
    def construct(self):
        # ------------------------------------------------------------
        # PARÂMETROS DA ELIPSE
        # ------------------------------------------------------------
        a = 3.25                   # semi-eixo maior
        b = 2.05                   # semi-eixo menor
        c = np.sqrt(a**2 - b**2)   # distância do centro a cada foco

        centro = UP * 2.2
        f1_pos = centro + LEFT * c
        f2_pos = centro + RIGHT * c

        titulo = Text(
            "A propriedade focal da elipse",
            font_size=34,
            color=WHITE,
        ).to_edge(UP, buff=0.55)

        subtitulo = Text(
            "Raios que partem de um foco chegam ao outro",
            font_size=22,
            color=GRAY_B,
        ).next_to(titulo, DOWN, buff=0.18)

        elipse = Ellipse(
            width=2 * a,
            height=2 * b,
            color=BLUE_B,
            stroke_width=5,
        ).move_to(centro)

        foco_1 = Dot(f1_pos, color=YELLOW, radius=0.11)
        foco_2 = Dot(f2_pos, color=YELLOW, radius=0.11)

        nome_f1 = MathTex("F_1", color=YELLOW).scale(0.75)
        nome_f1.next_to(foco_1, DOWN, buff=0.15)

        nome_f2 = MathTex("F_2", color=YELLOW).scale(0.75)
        nome_f2.next_to(foco_2, DOWN, buff=0.15)

        legenda = Text(
            "10 bolas saem de F₁, refletem na borda\ne convergem para F₂.",
            font_size=25,
            line_spacing=1.1,
            color=WHITE,
        ).move_to(DOWN * 2.15)

        self.play(
            FadeIn(titulo, shift=DOWN),
            FadeIn(subtitulo, shift=DOWN),
        )
        self.play(
            Create(elipse),
            FadeIn(foco_1),
            FadeIn(foco_2),
            Write(nome_f1),
            Write(nome_f2),
            run_time=1.8,
        )
        self.play(FadeIn(legenda), run_time=0.7)
        self.wait(0.5)

        # ------------------------------------------------------------
        # 10 BOLAS: F1 -> BORDA DA ELIPSE -> F2
        # ------------------------------------------------------------
        angulos = np.linspace(0.18, TAU - 0.18, 10)
        cores = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE, PINK, MAROON, GOLD]

        bolas = VGroup()
        rastros = VGroup()
        animacoes = []

        for angulo, cor in zip(angulos, cores):
            ponto_borda = centro + np.array([
                a * np.cos(angulo),
                b * np.sin(angulo),
                0,
            ])

            bola = Dot(f1_pos, radius=0.075, color=cor)
            rastro = TracedPath(
                bola.get_center,
                stroke_color=cor,
                stroke_width=2.8,
                stroke_opacity=[0.15, 1],
            )

            bolas.add(bola)
            rastros.add(rastro)

            trajeto_1 = Line(f1_pos, ponto_borda)
            trajeto_2 = Line(ponto_borda, f2_pos)

            animacoes.append(
                Succession(
                    MoveAlongPath(bola, trajeto_1, run_time=1.5),
                    MoveAlongPath(bola, trajeto_2, run_time=1.5),
                )
            )

        self.add(rastros, bolas)

        self.play(
            LaggedStart(*animacoes, lag_ratio=0.10),
            run_time=5.5,
        )
        self.wait(0.8)

        conclusao_1 = Text(
            "Independentemente da direção inicial,",
            font_size=24,
            color=WHITE,
        ).move_to(DOWN * 3.5)

        conclusao_2 = Text(
            "toda trajetória de F₁ encontra F₂.",
            font_size=27,
            color=YELLOW,
        ).next_to(conclusao_1, DOWN, buff=0.12)

        self.play(
            FadeOut(legenda),
            FadeIn(conclusao_1),
            FadeIn(conclusao_2),
        )
        self.wait(2)

        # ------------------------------------------------------------
        # TRANSIÇÃO PARA CURVAS DE NÍVEL
        # ------------------------------------------------------------
        self.play(FadeOut(VGroup(*self.mobjects)), run_time=1.2)

        titulo_2 = Text(
            "Demonstração por curvas de nível",
            font_size=32,
            color=WHITE,
        ).to_edge(UP, buff=0.55)

        formula = MathTex(
            r"f(P)=d(P,F_1)+d(P,F_2)",
            color=WHITE,
        ).scale(0.85).next_to(titulo_2, DOWN, buff=0.25)

        explicacao = Text(
            "No plano, as superfícies de nível são curvas.",
            font_size=20,
            color=GRAY_B,
        ).next_to(formula, DOWN, buff=0.15)

        centro_2 = DOWN * 0.8
        f1_2 = centro_2 + LEFT * c
        f2_2 = centro_2 + RIGHT * c

        plano = NumberPlane(
            x_range=[-4.1, 4.1, 1],
            y_range=[-3.4, 3.4, 1],
            x_length=8.0,
            y_length=6.8,
            background_line_style={
                "stroke_color": GRAY_E,
                "stroke_width": 1,
                "stroke_opacity": 0.35,
            },
        ).move_to(centro_2)

        foco_1_2 = Dot(f1_2, color=YELLOW, radius=0.10)
        foco_2_2 = Dot(f2_2, color=YELLOW, radius=0.10)

        f1_label_2 = MathTex("F_1", color=YELLOW).scale(0.7)
        f1_label_2.next_to(foco_1_2, DOWN, buff=0.13)

        f2_label_2 = MathTex("F_2", color=YELLOW).scale(0.7)
        f2_label_2.next_to(foco_2_2, DOWN, buff=0.13)

        self.play(
            FadeIn(titulo_2),
            Write(formula),
            FadeIn(explicacao),
            Create(plano),
            FadeIn(foco_1_2),
            FadeIn(foco_2_2),
            Write(f1_label_2),
            Write(f2_label_2),
            run_time=2,
        )

        # Curvas de nível de f(P) = d(P,F1) + d(P,F2).
        # Para f(P) = 2A, obtemos uma elipse de semi-eixo maior A.
        niveis_a = [2.60, 2.82, 3.04, 3.25]
        cores_niveis = [PURPLE_C, BLUE_C, TEAL_C, YELLOW]

        curvas_nivel = VGroup()

        for A, cor in zip(niveis_a, cores_niveis):
            B = np.sqrt(A**2 - c**2)

            curva = Ellipse(
                width=2 * A,
                height=2 * B,
                color=cor,
                stroke_width=3.5,
            ).move_to(centro_2)

            curvas_nivel.add(curva)

        texto_niveis = Text(
            "Cada curva mantém constante a soma\ndas distâncias até os dois focos.",
            font_size=22,
            color=WHITE,
            line_spacing=1.1,
        ).move_to(DOWN * 5.15)

        self.play(FadeIn(texto_niveis), run_time=0.7)

        for curva in curvas_nivel[:-1]:
            self.play(Create(curva), run_time=0.8)

        elipse_final = curvas_nivel[-1]
        self.play(Create(elipse_final), run_time=1.2)

        # ------------------------------------------------------------
        # PONTO P PERCORRE A ELIPSE FINAL
        # ------------------------------------------------------------
        parametro = ValueTracker(0.03)

        ponto_p = always_redraw(
            lambda: Dot(
                elipse_final.point_from_proportion(parametro.get_value()),
                color=RED,
                radius=0.10,
            )
        )

        segmento_f1 = always_redraw(
            lambda: DashedLine(
                f1_2,
                ponto_p.get_center(),
                color=ORANGE,
                dash_length=0.09,
                stroke_width=2.5,
            )
        )

        segmento_f2 = always_redraw(
            lambda: DashedLine(
                ponto_p.get_center(),
                f2_2,
                color=GREEN,
                dash_length=0.09,
                stroke_width=2.5,
            )
        )

        nome_p = always_redraw(
            lambda: MathTex("P", color=RED)
            .scale(0.72)
            .next_to(ponto_p, UP, buff=0.12)
        )

        igualdade = MathTex(
            r"d(P,F_1)+d(P,F_2)=2a",
            color=YELLOW,
        ).scale(0.82).move_to(DOWN * 6.35)

        self.play(
            FadeIn(segmento_f1),
            FadeIn(segmento_f2),
            FadeIn(ponto_p),
            FadeIn(nome_p),
            Write(igualdade),
        )

        self.play(
            parametro.animate.set_value(0.99),
            run_time=5,
            rate_func=linear,
        )

        frase_final = Text(
            "Logo, a elipse é o conjunto dos pontos P\n"
            "cuja soma das distâncias aos focos é constante.",
            font_size=24,
            color=WHITE,
            line_spacing=1.1,
        ).move_to(DOWN * 7.25)

        self.play(FadeIn(frase_final, shift=UP), run_time=1)
        self.wait(3)
