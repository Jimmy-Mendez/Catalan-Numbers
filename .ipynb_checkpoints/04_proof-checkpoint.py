from manimlib import *

class proof(Scene):
    def construct(self):
        dots = dict()
        var_index = 0
        line = DashedLine(start= np.array([-2., -2., 0.]), end=np.array([2, 2., 0.]), buff=0, color = '#FC6255')
        line_p = DashedLine(start= np.array([-2., -1., 0.]), end=np.array([1, 2., 0.]), buff=0, color = '#f48fff')
        pos_paths = Tex("{2n \choose n}")
        move_dot = Dot(np.array([-2, -2., 0]), radius=0.15, color= '#69cdff')
        for x in range(-2, 3):
            for y in range(-2, 3):
                dots[f"{var_index}"] = Dot(np.array([x, y, 0]))
                var_index = var_index + 1
        for dot in dots.values():
            self.play(FadeIn(dot, scale=0.5, run_time = 0.08))
        self.wait(0.5)
        self.play(pos_paths.animate.shift(3 * LEFT).scale(0.5))
        points_1 = [[1, 0, 0],[1, 0, 0],[0, 1, 0],[1, 0, 0],[0, 1, 0],[0, 1, 0],[1, 0, 0],[0, 1, 0]]
        points_2 = [[0, 1, 0],[0, 1, 0],[1, 0, 0],[0, 1, 0],[0, 1, 0],[1, 0, 0],[1, 0, 0],[1, 0, 0]]
        points_3 = [[1, 0, 0],[1, 0, 0],[0, 1, 0],[0, 1, 0],[0, 1, 0],[1, 0, 0],[0, 1, 0],[1, 0, 0]]
        
        # showing possible paths
        path_1 = []
        path_2 = []
        path_3 = []
        start = np.array([-2.,-2.,0])
        for point in points_1:
            end = np.add(start, point)
            self.play(ApplyMethod(move_dot.shift, np.array(point)), run_time = 0.3)
            path_1.append(Line(start= start, end= end, buff=0, color = '#ffeb69'))
            self.play(ShowCreation(path_1[-1], scale=0.5, run_time = 0.28))
            start = np.array(end)
        self.play(Uncreate(Group(*path_1), scale=0.5, run_time = 0.28))
        self.play(ApplyMethod(move_dot.move_to, np.array([-2., -2., 0.])), run_time = 0.3)
        start = np.array([-2.,-2.,0])
        for point in points_2:
            end = np.add(start, point)
            self.play(ApplyMethod(move_dot.shift, np.array(point)), run_time = 0.3)
            path_2.append(Line(start= start, end= end, buff=0, color = '#ffeb69'))
            self.play(ShowCreation(path_2[-1], scale=0.5, run_time = 0.28))
            start = np.array(end)
        save_path = Group(*path_2)
        save_path.save_state()
        self.play(Uncreate(Group(*path_2), scale=0.5, run_time = 0.28))
        self.play(ApplyMethod(move_dot.move_to, np.array([-2., -2., 0.])), run_time = 0.3)
        start = np.array([-2.,-2.,0])
        for point in points_3:
            end = np.add(start, point)
            self.play(ApplyMethod(move_dot.shift, np.array(point)), run_time = 0.3)
            path_3.append(Line(start= start, end= end, buff=0, color = '#ffeb69'))
            self.play(ShowCreation(path_3[-1], scale=0.5, run_time = 0.28))
            start = np.array(end)
        self.play(Uncreate(Group(*path_3), scale=0.5, run_time = 0.28))
        
        #showing possible up strokes   
        
        for points_list in [points_1,points_2,points_3]:
            lines = []
            var_index_2 = 0
            location = [-2., -2., 0]
            for point in points_list:
                if point == [0, 1, 0]:
                    lines.append(Line(start= np.array(location), end=np.add(location,[0, 1., 0.]), buff=0, color = '#ffeb69'))
                    var_index_2 = var_index_2 + 1
                location = np.add(location,point)
            group_lines = Group(*lines)
            self.play(ShowCreation(group_lines, scale=0.5, run_time = 0.28))
            self.wait(0.5)
            self.play(Uncreate(group_lines, scale=0.5, run_time = 0.28))
            
        for points_list in [points_1,points_2,points_3]:
            lines = []
            var_index_2 = 0
            location = [-2., -2., 0]
            for point in points_list:
                if point == [1, 0, 0]:
                    lines.append(Line(start= np.array(location), end=np.add(location,[1, 0., 0.]), buff=0, color = '#ffeb69'))
                    var_index_2 = var_index_2 + 1
                location = np.add(location,point)
            group_lines = Group(*lines)
            self.play(ShowCreation(group_lines, scale=0.5, run_time = 0.28))
            self.wait(0.5)
            self.play(Uncreate(group_lines, scale=0.5, run_time = 0.28))
        self.play(ShowCreation(line, scale=0.5, run_time = 0.28))
        self.play(line.animate.scale(1.25))
        self.play(line.animate.scale(.8))
        save_path.restore()
        self.play(ShowCreation(save_path, scale=0.5, run_time = 0.28))
        self.play(ShowCreation(line_p, scale=0.5, run_time = 0.28))
        flipped_points = [[-2,-1,0],[-1,-1,0],[-1,0,0],[0,0,0],[1,0,0],[1,1,0],[1,2,0],[1,3,0]]
        flipped_path = []
        count = 1
        for point in flipped_points:
            if point != [1,3,0]:
                flipped_path.append(Line(start = np.array(point), end=np.array(flipped_points[count]), buff=0, color = '#ff6a00'))
            count+=1
        group_lines_f = Group(*flipped_path)
        self.play(ShowCreation(group_lines_f, scale=0.5, run_time = 0.28))
            