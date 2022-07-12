from manimlib import *

class PathScene(Scene):
    def construct(self):
        dots = dict()
        var_index = 0
        for x in range(-2, 3):
            for y in range(-2, 3):
                dots[f"{var_index}"] = Dot(np.array([x, y, 0]))
                var_index = var_index + 1
        line = DashedLine(start= np.array([-2., -2., 0.]), end=np.array([2, 2., 0.]), buff=0, color = '#FC6255')
        circle_1 = Circle(color= '#ffffff', radius=0.2, arc_center=np.array([-2, -2., 0.]))
        circle_2 = Circle(color= '#ffffff', radius=0.2, arc_center=np.array([2, 2., 0.]))
        move_dot = Dot(np.array([-2., -2., 0]), radius=0.15, color= '#69cdff')
        arrow_1 = Arrow(start=np.array([-2., -2., 0.]), end=np.array([-1., -2., 0.]), color='#ffeb69', buff=0.0)
        arrow_2 = Arrow(start=np.array([-1., -2., 0.]), end=np.array([0., -2., 0.]), color='#ffeb69', buff=0.0)
        arrow_3 = Arrow(start=np.array([0, -2., 0.]), end=np.array([0., -1., 0.]), color='#ffeb69', buff=0.0)
        arrow_4 = Arrow(start=np.array([0., -1., 0.]), end=np.array([1., -1., 0.]), color='#ffeb69', buff=0.0)
        arrow_5 = Arrow(start=np.array([1., -1., 0.]), end=np.array([1., 0., 0.]), color='#ffeb69', buff=0.0)
        arrow_6 = Arrow(start=np.array([1., 0., 0.]), end=np.array([1., 1., 0.]), color='#ffeb69', buff=0.0)
        arrow_7 = Arrow(start=np.array([1., 1., 0.]), end=np.array([2., 1., 0.]), color='#ffeb69', buff=0.0)
        arrow_8 = Arrow(start=np.array([2., 1., 0.]), end=np.array([2., 2., 0.]), color='#ffeb69', buff=0.0)
        arrow_up = Arrow(start=np.array([3., 1., 0.]), end=np.array([3., 2., 0.]), color='#ffffff', buff=0.0)
        arrow_right = Arrow(start=np.array([3., -1., 0.]), end=np.array([4., -1., 0.]), color='#ffffff', buff=0.0)
        nxn = Tex("n*n")
        q = Text("?")
        VGroup(nxn, q).arrange(DOWN, buff=1)
        fxf = Tex("5*5")
        self.play(Write(nxn, run_time = 1))
        self.wait(1)
        self.play(Write(q, run_time = 1))
        self.wait(2)
        self.play(FadeOut(q), shift=DOWN)
        self.play(ReplacementTransform(nxn, fxf))
        self.play(fxf.animate.shift(3 * LEFT).scale(0.5))
        for dot in dots.values():
            self.play(FadeIn(dot, scale=0.5, run_time = 0.08))
        self.wait(0.5)
        self.play(ShowCreation(line))
        self.play(ShowCreation(circle_1))
        self.play(ShowCreation(circle_2))
        self.wait(2)
        self.play(Uncreate(circle_1))
        self.play(Uncreate(circle_2))
        self.play(FadeIn(move_dot, scale=0.5, run_time = 0.5))
        points = [[1, 0, 0],[1, 0, 0],[0, 1, 0],[1, 0, 0],[0, 1, 0],[0, 1, 0],[1, 0, 0],[0, 1, 0]]
        arrows = [arrow_1, arrow_2, arrow_3, arrow_4, arrow_5, arrow_6, arrow_7, arrow_8]
        for point, arrow in zip(points, arrows):
            self.play(ShowCreation(arrow), run_time = 0.3)
            self.play(ApplyMethod(move_dot.shift, np.array(point)), run_time = 0.3)
        self.wait(2)
        self.play(ShowCreation(arrow_up), run_time = 1)
        self.wait(.4)
        self.play(ShowCreation(arrow_right), run_time = 1)
        self.play(
            *[Uncreate(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
        
