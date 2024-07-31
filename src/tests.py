import unittest

from cell import Cell
from maze import Maze


class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    num_cols = 12
    num_rows = 10
    m1 = Maze(0,0, num_rows, num_cols, 10, 10)
    self.assertEqual(len(m1._cells), num_cols)
    self.assertEqual(len(m1._cells[0]), num_rows)

  def test_break_entrance_and_exit(self):
    num_cols = 12
    num_rows = 10
    m1 = Maze(0,0, num_rows, num_cols, 10, 10)
    self.assertEqual(len(m1._cells), num_cols)
    self.assertEqual(len(m1._cells[0]), num_rows)
    first_cell: Cell = m1._cells[0][0]
    self.assertEqual(first_cell.has_top_wall, False)
    last_cell: Cell = m1._cells[num_cols - 1][num_rows - 1]
    self.assertEqual(last_cell.has_bottom_wall, False)

  def test_reset_visisted(self):
    m1 = Maze(0,0, 10, 10, 10, 10)
    for i in range(m1._num_columns):
      for j in range(m1._num_rows):
        m1._cells[i][j].visited = True

    m1._reset_cells_visited()

    for i in range(m1._num_columns):
      for j in range(m1._num_rows):
        self.assertFalse(m1._cells[i][j].visited)

if __name__ == "__main__":
  unittest.main()