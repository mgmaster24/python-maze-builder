from primitives import Point, Line
from window import Window

class Cell:
    def __init__(self, top_left: Point, bottom_right: Point, win: Window) -> None:
        self.__top_left = top_left
        self.__bottom_right = bottom_right
        self.__win = win
        self.has_top_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True

    def draw(self, fill_color: str = "white") -> None:
        if self.has_left_wall:
            self.__win.draw_line(
                Line(
                    self.__top_left,
                    Point(self.__top_left.x, self.__bottom_right.y)), fill_color)
            
        if self.has_right_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__bottom_right.x, self.__top_left.y),
                    self.__bottom_right), fill_color)
            
        if self.has_top_wall:
            self.__win.draw_line(
                Line(
                    self.__top_left,
                    Point(self.__bottom_right.x, self.__top_left.y)), fill_color)
            
        if self.has_bottom_wall:
            self.__win.draw_line(
                Line(
                    Point(self.__top_left.x, self.__bottom_right.y),
                    self.__bottom_right), fill_color)
            