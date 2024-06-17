import math
from manim import *


class Introduction(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        title = Text(r"Natural Log Integration Trivia", color=BLACK)
        description = Tex(
            r"The two areas bounded by $y = \ln(x)$ from x = 0 to x = e are equal.", color=BLACK, font_size=36)
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


class FunctionPlot(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # plane = NumberPlane(color=BLACK)
        # self.add(plane)            

        axes = Axes(
            x_range=(-1, 5),
            y_range=(-5, 5),
            x_length=10,
            y_length=10,
            axis_config={"color": BLACK,
                         "include_numbers": True, "include_tip": False},
            x_axis_config={"numbers_to_include": []},
            y_axis_config={"numbers_to_include": []},
            tips=False
        )

        nl_axes = axes.get_axes()
        x_axis, y_axis = nl_axes[0], nl_axes[1]

        # for number in x_axis.numbers:
        #     number.set_color(BLACK)

        e_dot = Dot(point=x_axis.number_to_point(math.e, ), color=BLUE)
        e_label = MathTex(r"e", color=BLACK, font_size=36)
        e_label.next_to(e_dot, DOWN, buff=0.1)

        curve_t = MathTex(r"y = \ln(x)", color=BLACK)

        labels = axes.get_axis_labels(x_label="x", y_label="y")
        curve = axes.plot(lambda x: math.log(
            x), x_range=(0.001, 5, 0.001), color=RED)
        curve_t.next_to(curve.get_all_points()[-1], UP, buff=0.1)

        upper_limit_line = axes.get_vertical_line(
            axes.input_to_graph_point(math.e, curve), color=BLUE)

        area_1 = axes.get_area(curve, x_range=(0.01, 1), color=RED)
        area_2 = axes.get_area(curve, x_range=(1, math.e), color=BLUE)

        self.play(Create(axes), run_time=2)
        self.play(Create(curve), run_time=3)
        self.play(
            Write(curve_t),
            Write(upper_limit_line),
            Write(e_label),
            Write(e_dot)
        )
        self.play(
            FadeIn(area_1),
            FadeIn(area_2)
        )

        self.wait()

        # Display equation: Area 1 = Area 2

        c_area_1 = area_1.copy()
        c_area_1.generate_target()
        c_area_1.target.move_to(DOWN * 2).scale(0.6)

        self.add(c_area_1)
        self.play(MoveToTarget(c_area_1))

        self.wait()

        area_equal = MathTex(r"=", color=BLACK)
        area_equal.next_to(c_area_1, buff=-0.25)

        self.play(Write(area_equal))

        self.wait()

        c_area_2 = area_2.copy()
        c_area_2.generate_target()
        c_area_2.target.next_to(c_area_1, buff=-0.15).scale(0.6)

        self.add(c_area_2)
        self.play(MoveToTarget(c_area_2))

        self.wait()

        # Solve the upper limit of the first bounded area

        area_integrals = MathTex(r"\int_a^b \ln(x) dx", r"=", r"\int_b^c \ln(x) dx", color=BLACK)
        area_integrals[0].set_color(RED)
        area_integrals[2].set_color(BLUE)

        area_integrals.move_to(area_equal)

        area_transform_animation_1 = ReplacementTransform(c_area_1, area_integrals[0])
        area_transform_animation_2 = ReplacementTransform(c_area_2, area_integrals[2])

        area_integral_lb_1 = MathTex(r"\int_0^b \ln(x) dx", color=RED).move_to(area_integrals[0], UP + RIGHT)
        area_integral_ub_2 = MathTex(r"\int_b^e \ln(x) dx", color=BLUE).move_to(area_integrals[2], UP + RIGHT)

        integral_lb_transform_animation_1 = ReplacementTransform(area_integrals[0], area_integral_lb_1)
        integral_ub_transform_animation_2 = ReplacementTransform(area_integrals[2], area_integral_ub_2)

        self.play(area_transform_animation_1, area_transform_animation_2)

        self.wait()

        self.play(integral_lb_transform_animation_1, integral_ub_transform_animation_2)

        self.wait()

        area_integrals.generate_target()
        area_integrals.target.move_to(UP * 2)

        self.remove(area_equal, area_integral_lb_1, area_integral_ub_2)
        self.play(MoveToTarget(area_integrals))

        self.wait()

        # Start: Scene FunctionPlot_2

        equation_1 = MathTex(r"y", r"=", r"\ln(x)", color=BLACK)
        equation_2 = MathTex(r"0", r"=", r"\ln(x)", color=BLACK)
        equation_3 = MathTex(r"\ln(x)", r"=", r"0", color=BLACK)
        
        equation_1.move_to(DOWN)
        equation_2.move_to(DOWN)
        
        equation_3[1].move_to(equation_2[1])
        equation_3[0].next_to(equation_3[1], LEFT)
        equation_3[2].next_to(equation_3[1], RIGHT)

        self.play(Write(equation_1))

        self.wait()

        le_transform_animation_1 = ReplacementTransform(
            equation_1[0], equation_2[0])

        self.play(le_transform_animation_1)

        self.wait()

        equation_2[0].generate_target()
        equation_2[2].generate_target()

        equation_2[0].target.move_to(equation_3[2])
        equation_2[2].target.move_to(equation_3[0])

        self.remove(equation_1[0], equation_1[2])
        self.play(MoveToTarget(equation_2[0]), MoveToTarget(equation_2[2]))

        self.wait()

        equation_4 = MathTex(r"e^0", r"=", r"e^{\ln(x)}", color=BLACK)
        equation_4[1].move_to(equation_2[1])
        equation_4[0].next_to(equation_4[1], RIGHT)
        equation_4[2].next_to(equation_4[1], LEFT)

        equation_transform_animation_1 = ReplacementTransform(equation_2[0], equation_4[0])
        equation_transform_animation_2 = ReplacementTransform(equation_2[2], equation_4[2])

        self.play(equation_transform_animation_1, equation_transform_animation_2)

        self.wait()

        equation_5 = MathTex(r"1", r"=", r"x", color=BLACK)
        equation_5[1].move_to(equation_4[1])
        equation_5[0].next_to(equation_5[1], RIGHT)
        equation_5[2].next_to(equation_5[1], LEFT)

        equation_transform_animation_3 = ReplacementTransform(equation_4[0], equation_5[0])
        equation_transform_animation_4 = ReplacementTransform(equation_4[2], equation_5[2])

        self.play(equation_transform_animation_3, equation_transform_animation_4)
        
        # Insertion Start

        self.wait()
        
        area_integrals.generate_target()
        area_integrals.target.move_to(area_equal)

        self.play(MoveToTarget(area_integrals))

        self.wait()

        area_integral_ub_1 = MathTex(r"\int_0^1 \ln(x) dx", color=RED).move_to(area_integrals[0], UP + RIGHT)
        area_integral_lb_2 = MathTex(r"\int_1^e \ln(x) dx", color=BLUE).move_to(area_integrals[2], UP + RIGHT)

        integral_ub_transform_animation_1 = ReplacementTransform(area_integrals[0], area_integral_ub_1)
        integral_lb_transform_animation_2 = ReplacementTransform(area_integrals[2], area_integral_lb_2)

        self.play(integral_ub_transform_animation_1, integral_lb_transform_animation_2)

        # Insertion End
        
        self.wait()

        # End: Scene FunctionPlot_2

        surround_rectangle_1 = SurroundingRectangle(area_integrals[0], color=RED)
        surround_rectangle_2 = SurroundingRectangle(area_integrals[2], color=BLUE)

        self.play(Write(surround_rectangle_1, run_time=1))
        self.play(FadeOut(surround_rectangle_1, run_time=1))

        self.play(Write(surround_rectangle_2, run_time=1))
        self.play(FadeOut(surround_rectangle_2, run_time=1))

        self.wait()

        self.play(Indicate(area_1))

        self.wait()

        area_integral_r = MathTex(r"- \int_1^e \ln(x) dx", color=BLUE).move_to(area_integrals[2], UP + LEFT)

        area_integral_transform_animation_1 = ReplacementTransform(area_integrals[2], area_integral_r)

        self.play(area_integral_transform_animation_1)

        self.wait()

        area_integral_re_l = MathTex(r"\int_1^e \ln(x) dx", color=BLUE).move_to(area_integrals[0], UP + RIGHT)
        area_integral_re_r = MathTex(r"- \int_0^1 \ln(x) dx", color=RED).move_to(area_integrals[2], UP + RIGHT)

        area_integral_transform_animation_2 = ReplacementTransform(area_integrals[2], area_integral_re_l)
        area_integral_transform_animation_3 = ReplacementTransform(area_integrals[0], area_integral_re_r)

        self.play(area_integral_transform_animation_2, area_integral_transform_animation_3)

        self.wait()

        area_integrals_2 = MathTex(r"\int_1^e \ln(x) dx", r"+", r"\int_0^1 \ln(x) dx", r"=", r"0", color=BLACK)
        area_integrals_2[0].set_color(BLUE)
        area_integrals_2[2].set_color(RED)

        area_integrals_2.move_to(area_integrals)

        area_integral_transform_animation_4 = ReplacementTransform(area_integrals, area_integrals_2)

        self.play(area_integral_transform_animation_4)

        self.wait()

        area_integrals_3 = MathTex(r"\int_0^e \ln(x) dx", r"=", r"0", color=BLACK)

        area_integrals_3.move_to(area_integrals_2)

        area_integral_transform_animation_5 = ReplacementTransform(area_integrals_2, area_integrals_3)

        self.play(area_integral_transform_animation_5)

        self.wait(3)


class FunctionPlot_2(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        equation_1 = MathTex(r"y", r"=", r"\ln(x)", color=BLACK)
        equation_2 = MathTex(r"0", r"=", r"\ln(x)", color=BLACK)
        equation_3 = MathTex(r"\ln(x)", r"=", r"0", color=BLACK)
        
        equation_1.move_to(DOWN)
        equation_2.move_to(DOWN)
        
        equation_3[1].move_to(equation_2[1])
        equation_3[0].next_to(equation_3[1], LEFT)
        equation_3[2].next_to(equation_3[1], RIGHT)

        self.play(Write(equation_1))

        self.wait()

        le_transform_animation_1 = ReplacementTransform(
            equation_1[0], equation_2[0])

        self.play(le_transform_animation_1)

        self.wait()

        equation_2[0].generate_target()
        equation_2[2].generate_target()

        equation_2[0].target.move_to(equation_3[2])
        equation_2[2].target.move_to(equation_3[0])

        self.remove(equation_1[0], equation_1[2])
        self.play(MoveToTarget(equation_2[0]), MoveToTarget(equation_2[2]))

        self.wait()

        equation_4 = MathTex(r"e^0", r"=", r"e^{\ln(x)}", color=BLACK)
        equation_4[1].move_to(equation_2[1])
        equation_4[0].next_to(equation_4[1], RIGHT)
        equation_4[2].next_to(equation_4[1], LEFT)

        equation_transform_animation_1 = ReplacementTransform(equation_2[0], equation_4[0])
        equation_transform_animation_2 = ReplacementTransform(equation_2[2], equation_4[2])

        self.play(equation_transform_animation_1, equation_transform_animation_2)

        self.wait()

        equation_5 = MathTex(r"1", r"=", r"x", color=BLACK)
        equation_5[1].move_to(equation_4[1])
        equation_5[0].next_to(equation_5[1], RIGHT)
        equation_5[2].next_to(equation_5[1], LEFT)

        equation_transform_animation_3 = ReplacementTransform(equation_4[0], equation_5[0])
        equation_transform_animation_4 = ReplacementTransform(equation_4[2], equation_5[2])

        self.play(equation_transform_animation_3, equation_transform_animation_4)
        
        self.wait()


class FirstApproach(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        area_integrals_1 = MathTex(r"\int_0^e \ln(x) dx", r"=", r"0", color=BLACK)
        area_integrals_2 = MathTex(r"\int_1^e \ln(x) dx", r"=", r"- \int_0^1 \ln(x) dx", color=BLACK)

        area_integrals = VGroup(area_integrals_1, area_integrals_2).arrange(DOWN, buff=0.4)

        self.play(Write(area_integrals_1), Write(area_integrals_2))

        self.wait()

        surround_rectangle_1 = SurroundingRectangle(area_integrals_1, color=RED)
        surround_rectangle_2 = SurroundingRectangle(area_integrals_2, color=RED)

        self.play(Write(surround_rectangle_1), run_time=2)
        self.play(FadeOut(surround_rectangle_1), run_time=2)
        
        self.play(Write(surround_rectangle_2), run_time=2)
        self.play(FadeOut(surround_rectangle_2), run_time=2)

        self.wait()

        area_integrals_1.generate_target()
        area_integrals_1.target.to_edge(UP)

        self.play(FadeOut(area_integrals_2), MoveToTarget(area_integrals_1))

        self.wait()

        integration_by_parts = MathTex(r"\int", r"u", r"dv", r"=", r"u", r"v", r"-", r"\int", r"v", r"du", color=BLACK)
        integration_by_parts.move_to(UP)

        self.play(Write(integration_by_parts))

        let_u = MathTex(r"u", r"=", r"\ln(x)", color=BLACK)
        let_dv = MathTex(r"dv", r"=", r"dx", color=BLACK)

        thus_du = MathTex(r"du", r"=", r"\frac{d}{dx} \ln(x)", color=BLACK)
        # thus_v = MathTex(r"v", r"=", r"\int", r"dx", color=BLACK)
        thus_v = MathTex(r"v", r"=", r"x", color=BLACK)

        let_u.move_to(DOWN + LEFT * 2)
        thus_du.move_to(DOWN + RIGHT * 2)

        let_dv.move_to(DOWN * 2.5 + LEFT * 2)
        thus_v.move_to(DOWN * 2.5 + RIGHT * 2)

        self.play(Write(let_u))
        self.play(Write(let_dv))
        self.play(Write(thus_du))
        self.play(Write(thus_v))

        # Substitue u

        indicator_box = SurroundingRectangle(let_u, color=RED)
        _integration_by_parts = MathTex(r"\int", r"\ln(x)", r"dv", r"=", r"\ln(x)", r"v", r"-", r"\int", r"v", r"du", color=BLACK).move_to(integration_by_parts)

        self.play(Write(indicator_box), run_time=2)
        self.play(Transform(integration_by_parts, _integration_by_parts))        
        self.play(FadeOut(indicator_box), run_time=2)

        # Substitue dv

        indicator_box = SurroundingRectangle(let_dv, color=RED)
        _integration_by_parts = MathTex(r"\int", r"\ln(x)", r"dx", r"=", r"\ln(x)", r"\cdot", r"v", r"-", r"\int", r"v", r"du", color=BLACK).move_to(integration_by_parts)
        
        self.play(Write(indicator_box), run_time=2)
        self.play(Transform(integration_by_parts, _integration_by_parts))        
        self.play(FadeOut(indicator_box), run_time=2)

        # Substitue du

        indicator_box = SurroundingRectangle(thus_du, color=RED)        
        _integration_by_parts = MathTex(r"\int", r"\ln(x)", r"dx", r"=", r"\ln(x)", r"\cdot", r"v", r"-", r"\int", r"v", r"\frac{1}{x}", r"dx", color=BLACK).move_to(integration_by_parts)
        
        self.play(Write(indicator_box), run_time=2)
        self.play(Transform(integration_by_parts, _integration_by_parts))        
        self.play(FadeOut(indicator_box), run_time=2)

        # Substitute v

        indicator_box = SurroundingRectangle(thus_v, color=RED)
        _integration_by_parts = MathTex(r"\int", r"\ln(x)", r"dx", r"=", r"\ln(x)", r"\cdot", r"x", r"-", r"\int", r"x", r"\cdot", r"\frac{1}{x}", r"dx", color=BLACK).move_to(integration_by_parts)
        
        self.play(Write(indicator_box), run_time=2)
        self.play(Transform(integration_by_parts, _integration_by_parts))        
        self.play(FadeOut(indicator_box), run_time=2)

        # After Substitution

        integration_by_parts.generate_target()
        integration_by_parts.target.shift(DOWN)

        self.wait()

        self.play(FadeOut(let_u), FadeOut(let_dv), FadeOut(thus_du), FadeOut(thus_v))
        self.play(MoveToTarget(integration_by_parts))
        
        self.wait()

        _integration_by_parts = MathTex(r"\int", r"\ln(x)", r"dx", r"=", r"\ln(x)", r"\cdot", r"x", r"-", r"\int", r"dx", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts))

        self.wait()

        _integration_by_parts = MathTex(r"\int", r"\ln(x)", r"dx", r"=", r"\ln(x)", r"\cdot", r"x", r"-", r"x", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts)) 

        self.wait()

        # Evaluation               

        _integration_by_parts = MathTex(r"\int_a^b", r"\ln(x)", r"dx", r"=", r"\Big|_a^b", r"\ln(x)", r"\cdot", r"x", r"-", r"x", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts))

        _integration_by_parts = MathTex(r"\int_0^e", r"\ln(x)", r"dx", r"=", r"\Big|_0^e", r"\ln(x)", r"\cdot", r"x", r"-", r"x", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts)) 

        self.wait(2)


class FirstApproach_Eval(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        integration_by_parts = MathTex(r"\int_0^e", r"\ln(x)", r"dx", r"=", r"\Big|_0^e", r"\ln(x)", r"\cdot", r"x", r"-", r"x", color=BLACK)

        self.add(integration_by_parts)

        self.wait()

        _integration_by_parts = MathTex(r"\int_0^e", r"\ln(x)", r"dx", r"=", r"[(\ln(e) \cdot e - e) - (\ln(0) \cdot 0 - 0)]", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts)) 

        self.wait()

        _integration_by_parts = MathTex(r"\int_0^e", r"\ln(x)", r"dx", r"=", r"[(e - e) - (0 - 0)]", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts)) 

        self.wait()

        _integration_by_parts = MathTex(r"\int_0^e", r"\ln(x)", r"dx", r"=", r"0", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts)) 

        self.wait(2)


class SecondApproach_Eval_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        area_integrals = MathTex(r"\int_1^e \ln(x) dx", r"=", r"- \int_0^1 \ln(x) dx", color=BLACK)
        
        area_integrals.generate_target()
        area_integrals.target.to_edge(UP)

        self.play(MoveToTarget(area_integrals))
        
        self.wait()
         
        integration_by_parts = MathTex(r"\int_0^1", r"\ln(x)", r"dx", r"=", r"\Big|_0^1", r"\ln(x)", r"\cdot", r"x", r"-", r"x", color=BLACK)

        self.play(Write(integration_by_parts))

        self.wait()

        _integration_by_parts = MathTex(r"\int_0^1", r"\ln(x)", r"dx", r"=", r"[(\ln(1) \cdot 1 - 1) - (\ln(0) \cdot 0 - 0)]", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts)) 

        self.wait()

        _integration_by_parts = MathTex(r"\int_0^1", r"\ln(x)", r"dx", r"=", r"[(0 \cdot 1 - 1) - (0 - 0)]", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts)) 

        self.wait()

        _integration_by_parts = MathTex(r"\int_0^1", r"\ln(x)", r"dx", r"=", r"- 1 - 0", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts)) 

        self.wait()

        _integration_by_parts = MathTex(r"\int_0^1", r"\ln(x)", r"dx", r"=", r"-1", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts))

        self.wait()

        integration_by_parts.generate_target()
        integration_by_parts.target.move_to(DOWN * 2 + LEFT * 3)

        self.play(MoveToTarget(integration_by_parts))

        self.wait(2)


class SecondApproach_Eval_2(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        area_integrals = MathTex(r"\int_1^e \ln(x) dx", r"=", r"- \int_0^1 \ln(x) dx", color=BLACK)
        prev_integration_by_parts = MathTex(r"\int_0^1", r"\ln(x)", r"dx", r"=", r"-1", color=BLACK)

        area_integrals.to_edge(UP)
        prev_integration_by_parts.move_to(DOWN * 2 + LEFT * 3)

        self.add(area_integrals, prev_integration_by_parts)
        
        self.wait()
         
        integration_by_parts = MathTex(r"\int_1^e", r"\ln(x)", r"dx", r"=", r"\Big|_1^e", r"\ln(x)", r"\cdot", r"x", r"-", r"x", color=BLACK)

        self.play(Write(integration_by_parts))

        self.wait()

        _integration_by_parts = MathTex(r"\int_1^e", r"\ln(x)", r"dx", r"=", r"[(\ln(e) \cdot e - e) - (\ln(1) \cdot 1 - 1)]", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts)) 

        self.wait()

        _integration_by_parts = MathTex(r"\int_1^e", r"\ln(x)", r"dx", r"=", r"[(e - e) - (0 - 1)]", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts)) 

        self.wait()

        _integration_by_parts = MathTex(r"\int_1^e", r"\ln(x)", r"dx", r"=", r"0 + 1", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts)) 

        self.wait()

        _integration_by_parts = MathTex(r"\int_1^e", r"\ln(x)", r"dx", r"=", r"1", color=BLACK).move_to(integration_by_parts)
        self.play(Transform(integration_by_parts, _integration_by_parts))

        self.wait()

        integration_by_parts.generate_target()
        integration_by_parts.target.move_to(DOWN * 2 + RIGHT * 3)

        self.play(MoveToTarget(integration_by_parts))

        self.wait(2)


class Conclusion(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        area_integrals = MathTex(r"\int_1^e \ln(x) dx", r"=", r"- \int_0^1 \ln(x) dx", color=BLACK)
        prev_integration_by_parts_1 = MathTex(r"\int_0^1", r"\ln(x)", r"dx", r"=", r"-1", color=BLACK)
        prev_integration_by_parts_2 = MathTex(r"\int_1^e", r"\ln(x)", r"dx", r"=", r"1", color=BLACK)

        area_integrals.to_edge(UP)
        prev_integration_by_parts_1.move_to(DOWN * 2 + LEFT * 3)
        prev_integration_by_parts_2.move_to(DOWN * 2 + RIGHT * 3)

        self.add(area_integrals, prev_integration_by_parts_1, prev_integration_by_parts_2)

        self.wait()

        indicator_box = SurroundingRectangle(prev_integration_by_parts_1, color=RED)
        
        area_integrals.generate_target()
        area_integrals.target.shift(DOWN * 3)

        self.play(MoveToTarget(area_integrals))

        self.wait()

        self.play(Write(indicator_box), run_time=2)

        _area_integrals = MathTex(r"\int_1^e \ln(x) dx", r"=", r"-(-1)", color=BLACK).move_to(area_integrals)
        self.play(Transform(area_integrals, _area_integrals))

        self.wait()

        _area_integrals = MathTex(r"\int_1^e \ln(x) dx", r"=", r"1", color=BLACK).move_to(area_integrals)
        self.play(Transform(area_integrals, _area_integrals))

        self.wait()

        self.play(FadeOut(indicator_box), run_time=2)

        indicator_box = SurroundingRectangle(prev_integration_by_parts_2, color=RED)
        
        self.play(Write(indicator_box), run_time=2)

        _area_integrals = MathTex(r"1", r"=", r"1", color=BLACK).move_to(area_integrals)
        self.play(Transform(area_integrals, _area_integrals))

        self.wait(2)


class Credits(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        thanks = Text("Thank You for Listening", color=BLACK, font_size=58, weight=BOLD)

        self.play(Write(thanks))

        self.wait(3)

        self.play(FadeOut(thanks))

        cred = Text("Credits", color=BLACK, font_size=58, weight=BOLD)
        cred.generate_target()
        cred.target.to_edge(UP)

        self.play(Write(cred))

        self.wait(3)

        self.play(MoveToTarget(cred))

        self.wait()

        author1 = Text("Ernest Louis Villacorta", color=BLACK, font_size=36, weight=BOLD)
        author1_desc = Text("Script, Animation, and Editing", color=BLACK, font_size=24)

        author2 = Text("Marc Paolo Mino", color=BLACK, font_size=36, weight=BOLD)
        author2_desc = Text("Drafting of Script", color=BLACK, font_size=24)

        author3 = Text("Ralph Joseph Roa", color=BLACK, font_size=36, weight=BOLD)
        author3_desc = Text("Voice Recording", color=BLACK, font_size=24)

        VGroup(author1, author1_desc, author2, author2_desc, author3, author3_desc).arrange(DOWN)

        self.play(
            Write(author1),
            Write(author1_desc),
            Write(author2),
            Write(author2_desc),
            Write(author3),
            Write(author3_desc)
        )

        manim_cred = Text("Powered by Manim", color=BLACK, font_size=24)
        capcut_cred = Text("Video edited on Capcut", color=BLACK, font_size=24)

        VGroup(manim_cred, capcut_cred).arrange(DOWN).move_to(DOWN * 3)

        self.play(Write(manim_cred), Write(capcut_cred))

        self.wait(2)