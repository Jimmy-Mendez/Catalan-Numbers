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
        points_1 = [[1, 0, 0],[1, 0, 0],[0, 1, 0],[1, 0, 0],[0, 1, 0],[0, 1, 0],[0, 1, 0],[1, 0, 0]]
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
        save_path_3 = Group(*path_1)
        save_path_3.save_state()
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
        save_path_2 = Group(*path_3)
        save_path_2.save_state()
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
        group_lines_f = self.flip_path(flipped_points)
        self.play(ShowCreation(group_lines_f, scale=0.5, run_time = 0.28))
        self.play(ApplyMethod(move_dot.shift, [-1,1,0]), run_time = 0.3)
        new_final = Tex("(3,5)")
        new_final.shift([2,3,0])
        new_final_t = Tex("(n-1,n+1)")
        new_final_t.shift([3,3,0])
        self.play(ShowCreation(new_final, scale=0.5, run_time = 0.28))
        self.play(ReplacementTransform(new_final, new_final_t))
        uncreate_group = Group(*new_final_t, group_lines_f, *save_path)
        self.play(Uncreate(uncreate_group))
        
        save_path_3.restore()
        self.play(ShowCreation(save_path_3, scale=0.5, run_time = 0.28))
        flipped_points_2 = [[1,2,0],[1,3,0]]
        group_lines_f_2 = self.flip_path(flipped_points_2)
        self.play(ShowCreation(group_lines_f_2, scale=0.5, run_time = 0.28))
        uncreate_group_2 = Group(*save_path_3, group_lines_f_2)
        self.play(Uncreate(uncreate_group_2))
        
        save_path_2.restore()
        self.play(ShowCreation(save_path_2, scale=0.5, run_time = 0.28))
        flipped_points_3 = [[0,1,0],[0,2,0],[1,2,0],[1,3,0]]
        group_lines_f_3 = self.flip_path(flipped_points_3)
        self.play(ShowCreation(group_lines_f_3, scale=0.5, run_time = 0.28))
        uncreate_group_3 = Group(*save_path_2, group_lines_f_3)
        self.play(Uncreate(uncreate_group_3))
        
    def flip_path(self, points_list):
        flipped_path = []
        count = 1
        for point in points_list:
            if point != points_list[-1]:
                flipped_path.append(Line(start = np.array(point), end=np.array(points_list[count]), buff=0, color = '#ff6a00'))
            count+=1
        return Group(*flipped_path)
        
        
            