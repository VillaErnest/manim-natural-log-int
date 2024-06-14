from manim import *

class Introduction(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        title = Text(r"Natural Log Integration Trivia", color=BLACK)
        description = Tex(r"The two areas bounded by $y = \ln(x)$ from x = 0 to x = e are equal.", color=BLACK, font_size=36)
        curve = MathTex(r"y = \ln(x)", color=BLACK, font_size=36)
        authors = Text(r"Authors", color=BLACK, font_size=18, weight=BOLD)
        author_1 = Text(r"Ernest Louis Villacorta", color=BLACK, font_size=18)
        author_2 = Text(r"Ralph Joseph Roa", color=BLACK, font_size=18)
        author_3 = Text(r"Marc Paolo Mino", color=BLACK, font_size=18)

        header = VGroup(title, description, curve).arrange(DOWN)
        body = VGroup(authors, author_1, author_2, author_3).arrange(DOWN)

        VGroup(header, body).arrange_submobjects(DOWN, buff=0.5)

        self.play(
            Write(title),
            Write(description),
            Write(authors),
            Write(author_1),
            Write(author_2),
            Write(author_3),
            FadeIn(curve, shift=DOWN),
        )

        self.wait()


