import unittest

from maze import Maze
from point import Point


class Tests(unittest.TestCase):
    # testing the assignment for the top-left coordinate [x,y]:
    def test_maze_constructor_1(self):
        pnt = Point(8, 8)

        mz_1 = Maze(pnt, 4, 4, 10, 10)
        self.assertEqual(
            mz_1._p.x,
            pnt.x,
        )
        self.assertEqual(
            mz_1._p.y,
            pnt.y,
        )

    # testing the assignment for cell sizes:
    def test_maze_constructor_2(self):
        szx = 5
        szy = 5

        mz_1 = Maze(Point(8, 8), 4, 4, szx, szy)
        self.assertEqual(
            mz_1._cell_sz_x,
            szx,
        )
        self.assertEqual(
            mz_1._cell_sz_y,
            szy,
        )

    # testing the assignment for the number of rows and columns (1):
    def test_maze_create_cells_1(self):
        num_cols = 15
        num_rows = 10

        mz_1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(mz_1._cells),
            num_rows,
        )
        self.assertEqual(
            len(mz_1._cells[0]),
            num_cols,
        )

    # testing the assignment for the number of rows and columns (2):
    def test_maze_create_cells_2(self):
        num_cols = 35
        num_rows = 13

        mz_1 = Maze(Point(30, 45), num_rows, num_cols, 5, 5)
        self.assertEqual(
            len(mz_1._cells),
            num_rows,
        )
        self.assertEqual(
            len(mz_1._cells[0]),
            num_cols,
        )

    # testing if entry/exit walls are being broken successfully:
    def test_maze_break_entrance_and_exit(self):
        mz_1 = Maze(Point(30, 45), 15, 15, 5, 5)

        self.assertEqual(
            mz_1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            mz_1._cells[mz_1._num_rows - 1][mz_1._num_cols - 1].has_bottom_wall,
            False,
        )

    # testing the resetting of the visited status for the cells:
    def test_reset_cells_visited(self):
        num_cols = 15
        num_rows = 15

        mz_1 = Maze(Point(30, 45), num_rows, num_cols, 5, 5)

        for r in range(0, mz_1._num_rows):
            for c in range(0, mz_1._num_cols):
                self.assertEqual(mz_1._cells[r][c]._visited, False)


if __name__ == "__main__":
    unittest.main()
