from primitives import Line, Point
from window import Window


class Cell:
    def __init__(self, top_left: Point, bottom_right: Point, win: Window) -> None:
        self._top_left = top_left
        self._bottom_right = bottom_right
        half_length = (self._bottom_right.x - self._top_left.x) * 0.5
        self._center = Point(half_length + self._top_left.x, half_length + self._top_left.y)
        self._win = win
        self.has_top_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def center(self) -> Point:
        return self._center

    def draw(self, fill_color: str = "white") -> None:
        if self.has_left_wall:
            self._win.draw_line(
                Line(
                    self._top_left,
                    Point(self._top_left.x, self._bottom_right.y)), fill_color)
        else:
            self._win.draw_line(
                Line(
                    self._top_left,
                    Point(self._top_left.x, self._bottom_right.y)), self._win.bg_color)

        if self.has_right_wall:
            self._win.draw_line(
                Line(
                    Point(self._bottom_right.x, self._top_left.y),
                    self._bottom_right), fill_color)
        else:
            self._win.draw_line(
                Line(
                    Point(self._bottom_right.x, self._top_left.y),
                    self._bottom_right), self._win.bg_color)

        if self.has_top_wall:
            self._win.draw_line(
                Line(
                    self._top_left,
                    Point(self._bottom_right.x, self._top_left.y)), fill_color)
        else:
            self._win.draw_line(
                Line(
                    self._top_left,
                    Point(self._bottom_right.x, self._top_left.y)), self._win.bg_color)

        if self.has_bottom_wall:
            self._win.draw_line(
                Line(
                    Point(self._top_left.x, self._bottom_right.y),
                    self._bottom_right), fill_color)
        else:
            self._win.draw_line(
                Line(
                    Point(self._top_left.x, self._bottom_right.y),
                    self._bottom_right), self._win.bg_color)

    def draw_move(self, to_cell, undo: bool = False) -> None:
        color = "red"
        if undo:
            color = "gray"

        self._win.draw_line(Line(self._center, to_cell.center()), color)
