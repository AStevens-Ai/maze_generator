from cell_class import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win,):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self.cells = []

        self._create_cells()
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cells(i, j)
        self._break_entrance_and_exit() 
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._break_walls_r(i, j)

        self._reset_cells_visited()

    def _create_cells(self):
        
        for row in range(self.num_rows):
            row_cells = []
            for col in range(self.num_cols):

                x1 = self.x1 + col * self.cell_size_x
                y1 = self.y1 + row * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
        

                cell = Cell(x1, x2, y1, y2, self._win)
                cell.visited = False
                row_cells.append(cell)

            self.cells.append(row_cells)

    def _draw_cells(self, i, j):
        cell = self.cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        entrance_cell = self.cells[0][0]
        exit_cell = self.cells[self.num_rows - 1][self.num_cols - 1]

        entrance_cell.isEntrance = True
        exit_cell.isExit = True

        entrance_cell.draw()
        exit_cell.draw()
        self._animate()

    def _break_walls_r(self, i, j):
        current_cell = self.cells[i][j]
        current_cell.visited = True

        cond = True
        while cond:
            need_visit = []
            directions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for new_i, new_j in directions:
                if 0 <= new_i < self.num_rows and 0 <= new_j < self.num_cols:
                    neighbor_cell = self.cells[new_i][new_j]
                    if not neighbor_cell.visited:
                        need_visit.append((new_i, new_j))

            if not need_visit:
                cond = False
            
            if need_visit:
                next_i, next_j = random.choice(need_visit)
                next_cell = self.cells[next_i][next_j]
                
                if next_i == i - 1:
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                elif next_i == i + 1: 
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                elif next_j == j - 1: 
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                elif next_j == j + 1:
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                
                current_cell.draw()
                next_cell.draw()
                
                self._break_walls_r(next_i, next_j)

                

    def _reset_cells_visited(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.cells[row][col].visited = False

    def solve(self):
        i = 0 
        j = 0

        result =  self._solve_r(i, j)
        print(result)
        return result

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self.cells[i][j]
        current_cell.visited = True

        if current_cell.isExit:
            return True

        directions = [
        (i - 1, j, current_cell.has_top_wall, self.cells[i - 1][j].has_bottom_wall if i - 1 >= 0 else True),  # Up
        (i + 1, j, current_cell.has_bottom_wall, self.cells[i + 1][j].has_top_wall if i + 1 < len(self.cells) else True),  # Down
        (i, j - 1, current_cell.has_left_wall, self.cells[i][j - 1].has_right_wall if j - 1 >= 0 else True),  # Left
        (i, j + 1, current_cell.has_right_wall, self.cells[i][j + 1].has_left_wall if j + 1 < len(self.cells[0]) else True)   # Right
       ]

        for new_i, new_j, current_wall, neighbor_wall in directions:
            if (0 <= new_i < len(self.cells) and
                0 <= new_j < len(self.cells[0]) and
                not self.cells[new_i][new_j].visited and  
                not current_wall and  
                not neighbor_wall):
                
                current_cell.draw_move(self.cells[new_i][new_j], undo=False)

                if self._solve_r(new_i, new_j):
                    return True

                current_cell.draw_move(self.cells[new_i][new_j], undo=True)

        return False

                    
        
