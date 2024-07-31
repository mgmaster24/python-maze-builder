from maze import Maze
from window import Window


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_x_size = (screen_x - 2 * margin) / num_cols
    cell_y_size = (screen_y - 2 * margin) / num_rows

    win = Window(screen_x, screen_y, "Hello From Python")
    maze = Maze(margin, margin, num_rows, num_cols, cell_x_size, cell_y_size, win)
    maze.solve()

    win.wait_for_close()

main()