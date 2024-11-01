from point_class import Point
from line_class import Line

class Cell:
    def __init__(self, x1=0, x2=0, y1=0, y2=0, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.isEntrance = False
        self.isExit = False
        self.visited = False
       
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        
        self._win = win
    
    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1),Point(self._x1, self._y2))
            if self.isExit:
                self._win.draw_line(line, "black")
            elif self.isEntrance: 
                self._win.draw_line(line, "green")
            else:
                self._win.draw_line(line, "black")
        elif not self.has_left_wall:
            line = Line(Point(self._x1, self._y1),Point(self._x1, self._y2))
            if self.isExit:
                self._win.draw_line(line, "white")
            elif self.isEntrance: 
                self._win.draw_line(line, "white")
            else:
                self._win.draw_line(line, "white")
                
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            if self.isExit:
                self._win.draw_line(line, "red")
            elif self.isEntrance: 
                self._win.draw_line(line, "black")
            else:
                self._win.draw_line(line, "black")
        elif not self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            if self.isExit:
                self._win.draw_line(line, "white")
            elif self.isEntrance: 
                self._win.draw_line(line, "white")
            else:
                self._win.draw_line(line, "white")
        
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            if self.isExit:
                self._win.draw_line(line, "black")
            elif self.isEntrance: 
                self._win.draw_line(line, "black")
            else:
                self._win.draw_line(line, "black")
        elif not self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            if self.isExit:
                self._win.draw_line(line, "white")
            elif self.isEntrance: 
                self._win.draw_line(line, "white")
            else:
                self._win.draw_line(line, "white")
        
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            if self.isExit:
                self._win.draw_line(line, "black")
            elif self.isEntrance: 
                self._win.draw_line(line, "black")
            else:
                self._win.draw_line(line, "black")
        elif not self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            if self.isExit:
                self._win.draw_line(line, "white")
            elif self.isEntrance: 
                self._win.draw_line(line, "white")
            else:
                self._win.draw_line(line, "white")


        self._win.redraw()
    


    def draw_move(self, to_cell, undo=False):
        x_center = (self._x1 + self._x2) / 2
        y_center = (self._y2 + self._y1) / 2
        point1 = Point(x_center, y_center)
        other_x_center = (to_cell._x1 + to_cell._x2) / 2
        other_y_center = (to_cell._y1 + to_cell._y2) / 2
        point2 = Point(other_x_center, other_y_center)
        line = Line(point1, point2 )

        fill_color = "red"
        if undo:
            fill_color = "gray"
            
        self._win.draw_line(line, fill_color)