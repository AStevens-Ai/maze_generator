# This is a maze generator python gui, make sure to edit the main.py file, this is how you can launch a base 25x25 maze with box sizes of 30 by 30 in a 1920x1080 window follow the lower main.py code and copy it into main.py.
```
    win = Window(width=1920, height=1080)  
    x1, y1 = 100, 100
    num_rows, num_cols = 25, 25
    cell_size_x, cell_size_y = 30, 30
    
    maze = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()
    win.wait_for_close()
```
