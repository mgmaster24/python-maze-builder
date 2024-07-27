from tkinter import Tk, BOTH, Canvas
from primitives import Line

class Window:
    def __init__(self, width, height, title):
        self.__root = Tk()
        self.__root.title(title)
        self.__root.geometry(f'{width}x{height}')
        self.__root.config(bg='black')
        self.__canvas = Canvas(
            self.__root, 
            height=height, 
            width=width, 
            background="blue")
        self.__canvas.pack(fill=BOTH)
        self.__is_running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
    
    def close(self):
        self.__is_running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)