from maze_class import Maze
from window_class import Window 
def main():
    win = Window(width=1920, height=1080)  
    x1, y1 = 100, 100
    num_rows, num_cols = 25, 25
    cell_size_x, cell_size_y = 30, 30
    
    maze = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()
