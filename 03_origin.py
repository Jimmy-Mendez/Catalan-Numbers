from manimlib import *

class origin(Scene):
    def construct(self):
        eugene = SVGMobject("test.svg")
        vid = ImageMobject("vid.jpg")
        vid.scale(.6)
        link = Text("Link in description")
        des = ImageMobject("des.jpg")
        dyck = Text("Dyck Words")
        self.play(DrawBorderThenFill(eugene))
        self.play(eugene.animate.shift(3 * LEFT).scale(0.5))
        self.wait(2)
        Group(vid, link).arrange(DOWN, buff=1)
        self.play(FadeIn(vid))
        self.play(Write(link, run_time = 1))
        self.wait(5)
        self.play(
            *[Uncreate(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        Group(des, dyck).arrange(DOWN, buff=1)
        self.play(FadeIn(des))
        self.wait(2)
        self.play(Write(dyck, run_time = 1))
        self.wait(5)
        self.play(
            *[Uncreate(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
