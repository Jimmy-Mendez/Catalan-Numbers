from manimlib import *

class proof(Scene):
    def construct(self):
        dots = dict()
        var_index = 0
        line = DashedLine(start= np.array([-2., -2., 0.]), end=np.array([2, 2., 0.]), buff=0, color = '#FC6255')
        pos_paths = Tex("{2n \choose n}")
        move_dot = Dot(np.array([-2, -2., 0]), radius=0.15, color= '#69cdff')
        for x in range(-2, 3):
            for y in range(-2, 3):
                dots[f"{var_index}"] = Dot(np.array([x, y, 0]))
                var_index = var_index + 1
        for dot in dots.values():
            self.play(FadeIn(dot, scale=0.5, run_time = 0.08))
        self.wait(0.5)
        self.play(ShowCreation(line))
        self.play(pos_paths.animate.shift(3 * LEFT).scale(0.5))
        points_1 = [[1, 0, 0],[1, 0, 0],[0, 1, 0],[1, 0, 0],[0, 1, 0],[0, 1, 0],[1, 0, 0],[0, 1, 0]]
        points_2 = [[0, 1, 0],[0, 1, 0],[1, 0, 0],[0, 1, 0],[0, 1, 0],[1, 0, 0],[1, 0, 0],[1, 0, 0]]
        points_3 = [[1, 0, 0],[1, 0, 0],[0, 1, 0],[0, 1, 0],[0, 1, 0],[1, 0, 0],[0, 1, 0],[1, 0, 0]]
        
        # showing possible paths
        for point in points_1:
            self.play(ApplyMethod(move_dot.shift, np.array(point)), run_time = 0.3)
        self.play(ApplyMethod(move_dot.move_to, np.array([-2., -2., 0.])), run_time = 0.3)
        for point in points_2:
            self.play(ApplyMethod(move_dot.shift, np.array(point)), run_time = 0.3)
        self.play(ApplyMethod(move_dot.move_to, np.array([-2., -2., 0.])), run_time = 0.3)
        for point in points_3:
            self.play(ApplyMethod(move_dot.shift, np.array(point)), run_time = 0.3)
        
        #showing possible up strokes   
        
        lines = []
        var_index_2 = 0
        location = [-2., -2., 0]
        
        for point in points_1:
            if point == [0, 1, 0]:
                lines.append(Line(start= np.array(location), end=np.add(location,[0, 1., 0.]), buff=0, color = '#ffeb69'))
                var_index_2 = var_index_2 + 1
            location = np.add(location,point)
        group_lines = Group(*lines)
        self.play(ShowCreation(group_lines, scale=0.5, run_time = 0.28))