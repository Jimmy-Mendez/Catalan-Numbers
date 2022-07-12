from manimlib import *

class origin(Scene):
    def construct(self):
        eugene = SVGMobject("test.svg")
        self.play(DrawBorderThenFill(eugene))
        self.play(eugene.animate.shift(3 * LEFT).scale(0.5))
        vid= ImageMobject("vid.jpg")
        vid.scale(.6)
        self.play(FadeIn(vid))
        link = Text("Link in description")
        self.wait(5)
