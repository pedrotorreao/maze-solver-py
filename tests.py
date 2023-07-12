import unittest

from maze import Maze
from point import Point


class Tests(unittest.TestCase):
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

    def test_maze_create_cells_1(self):
        num_cols = 15
        num_rows = 10

        mz_1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(mz_1._cells),
            num_cols,
        )
        self.assertEqual(
            len(mz_1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        num_cols = 35
        num_rows = 13

        mz_1 = Maze(Point(30, 45), num_rows, num_cols, 5, 5)
        self.assertEqual(
            len(mz_1._cells),
            num_cols,
        )
        self.assertEqual(
            len(mz_1._cells[0]),
            num_rows,
        )


if __name__ == "__main__":
    unittest.main()
