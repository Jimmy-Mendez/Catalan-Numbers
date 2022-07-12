from manimlib import *

class sequence(Scene):
    def construct(self):
        CONFIG={
        "camera_config":{"background_color":"#000000"}
        }
        cat = Text("Catalan Numbers")
        eq = Tex("C_{n}=\\frac{(2n)!}{(n+1)!n!}")
        # eq_2 = Tex("C_{n}=\\prod_{k=2}^{n}\\frac{n+k}{n}")
        eq_3 = Tex("1, 1, 2, 5, 14, " , "42" , ", 132, 429, 1430, ...")
        self.play(Write(cat, run_time = 1))
        self.wait(1)
        self.play(cat.animate.shift(2 * UP).scale(0.5))
        self.play(Write(eq, run_time = 1))
        self.wait(2)
        # self.play(ReplacementTransform(eq, eq_2))
        # self.wait(2)
        self.play(ReplacementTransform(eq, eq_3))
        self.wait(2)
        self.play(eq_3[1].animate.scale(2).set_color(YELLOW), eq_3[0].animate.shift(0.4*LEFT), eq_3[2].animate.shift(0.4*RIGHT))
        self.wait(2)
        self.play(
            *[Uncreate(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )