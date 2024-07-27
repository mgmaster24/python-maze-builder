from window import Window
from primitives import Line, Point
from cell import Cell

def main():
    win = Window(800, 600, "Hello From Python")
    cell = Cell(Point(10, 10), Point(100, 100), win)
    cell.draw()
    win.wait_for_close()

main()