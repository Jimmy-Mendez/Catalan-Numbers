from manimlib import *

class proof_w(Scene):
    def construct(self):
        bad = Text("Bad paths:")
        p1 = Tex("{n-1+n+1 \choose n-1}", "=" , "{n-1+n+1 \choose n+1}")
        p2 = Tex("{2n \choose n-1}", "=", "{2n \choose n+1}")
        p3 = Tex("{2n \choose n}", "-", "{2n \choose n+1}")
        p4 = Tex("C_{n}", "=", "\\frac{1}{n+1}{2n \choose n}")
        self.play(Write(p1[0], run_time = 1))
        self.play(Write(p1[1], run_time = 1))
        self.play(Write(p1[2], run_time = 1))
        self.wait(3)
        self.play(ReplacementTransform(p1, p2))
        self.wait(3)
        VGroup(p2, p3, p4).arrange(DOWN, buff=1)
        self.play(Write(p3[0], run_time = 1))
        self.play(Write(p3[1], run_time = 1))
        self.play(Write(p3[2], run_time = 1))
        self.wait(3)
        self.play(Write(p4[2], run_time = 1))
        self.play(Write(p4[0], run_time = 1))
        self.play(Write(p4[1], run_time = 1))