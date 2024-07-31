import random
import time

from cell import Cell
from primitives import Point
from window import Window


class Maze:
  def __init__(
      self,
      x1: float,
      y1: float,
      num_rows: int,
      num_cols: int,
      cell_size_x: float,
      cell_size_y: float,
      win: Window = None,
      seed: int = None) -> None:
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_columns = num_cols
    self._cells = []
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    if seed:
      random.seed(seed)

    self._create_cells()
    self._break_entrance_and_exit()
    self._break_walls_r(0,0)
    self._reset_cells_visited()

  def _create_cells(self) -> None:
    for i in range(self._num_columns):
      col_cells = []
      for j in range(self._num_rows):
        x1: float = self._x1 + i * self._cell_size_x
        y1: float = self._y1 + j *self._cell_size_y
        x2: float =  x1 + self._cell_size_x
        y2: float = y1 + self._cell_size_y
        cell = Cell(Point(x1, y1), Point(x2, y2), self._win)
        col_cells.append(cell)
      self._cells.append(col_cells)

    for i in range(self._num_columns):
      for j in range(self._num_rows):
        self._draw_cells(i, j)

  def _draw_cells(self, i: int, j: int) -> None:
    if self._win is None:
      return

    cell: Cell = self._cells[i][j]
    cell.draw()
    self._animate()

  def _animate(self) -> None:
    if self._win is None:
      return

    self._win.redraw()
    time.sleep(0.03)

  def _break_entrance_and_exit(self) -> None:
    entry_cell: Cell = self._cells[0][0]
    entry_cell.has_top_wall = False
    self._draw_cells(0,0)

    exit_cell: Cell = self._cells[self._num_columns - 1][self._num_rows - 1]
    exit_cell.has_bottom_wall = False
    self._draw_cells(self._num_columns - 1, self._num_rows - 1)

  def _break_walls_r(self, i: int, j: int) -> None:
    current_cell: Cell = self._cells[i][j]
    current_cell.visited = True
    while True:
      possible_moves: list[tuple[int, int]] = []
      # left adjacent
      if i > 0 and not self._cells[i-1][j].visited:
        possible_moves.append((i-1, j))

      # right adjacent
      if i < self._num_columns - 1 and not self._cells[i+1][j].visited:
        possible_moves.append((i+1, j))

      # top adjacent
      if j > 0 and not self._cells[i][j-1].visited:
        possible_moves.append((i, j-1))

      # bottom adjacent
      if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
        possible_moves.append((i, j+1))

      if len(possible_moves) == 0:
        self._draw_cells(i, j)
        return

      direction: int = random.randrange(len(possible_moves))
      next_cell_indices: tuple[int, int] = possible_moves[direction]

      # left
      if next_cell_indices[0] == i-1:
        current_cell.has_left_wall = False
        self._cells[i-1][j].has_right_wall = False

      # right
      if next_cell_indices[0] == i+1:
        current_cell.has_right_wall = False
        self._cells[i+1][j].has_left_wall = False

      # top
      if next_cell_indices[1] == j-1:
        current_cell.has_top_wall = False
        self._cells[i][j-1].has_bottom_wall = False

      # bottom
      if next_cell_indices[1] == j+1:
        current_cell.has_bottom_wall = False
        self._cells[i][j+1].has_top_wall = False

      self._break_walls_r(next_cell_indices[0], next_cell_indices[1])

  def _reset_cells_visited(self) -> None:
    for i in range(self._num_columns):
      for j in range(self._num_rows):
        self._cells[i][j].visited = False

  def solve(self) -> bool:
    return self._solve_r(0,0)

  def _solve_r(self, i: int, j: int) -> bool:
    self._animate()
    current_cell: Cell = self._cells[i][j]
    current_cell.visited = True

    if (i == self._num_columns - 1 and j == self._num_rows - 1):
      return True

    if i > 0 and not current_cell.has_left_wall:
      adjCell: Cell = self._cells[i-1][j]
      if not adjCell.visited:
        current_cell.draw_move(adjCell)
        if self._solve_r(i-1, j):
          return True
        else:
          current_cell.draw_move(adjCell, True)

    if i < self._num_columns - 1 and not current_cell.has_right_wall:
      adjCell = self._cells[i+1][j]
      if not adjCell.visited:
        current_cell.draw_move(self._cells[i+1][j])
        if self._solve_r(i+1, j):
          return True
        else:
          current_cell.draw_move(self._cells[i+1][j], True)

    if j > 0 and not current_cell.has_top_wall:
      adjCell: Cell = self._cells[i][j-1]
      if not adjCell.visited:
        current_cell.draw_move(adjCell)
        if self._solve_r(i, j-1):
          return True
        else:
          current_cell.draw_move(adjCell, True)

    if j < self._num_rows - 1 and not current_cell.has_bottom_wall:
      adjCell: Cell = self._cells[i][j+1]
      if not adjCell.visited:
        current_cell.draw_move(adjCell)
        if self._solve_r(i, j+1):
          return True
        else:
          current_cell.draw_move(adjCell, True)

    return False

