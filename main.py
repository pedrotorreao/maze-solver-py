# import resources:
from window import Window
from point import Point
from cell import Cell
from maze import Maze


def main():
    wdw = Window(1000, 1000)

    mz = Maze(wdw, Point(100, 100), 10, 10, 50, 50)
    # mz._create_cells()

    # cell_1 = Cell(wdw, Point(50, 50), Point(100, 100))
    # cell_1.draw("black")

    # cell_2 = Cell(wdw, Point(100, 50), Point(150, 100))
    # cell_2.draw("black")
    # cell_1.draw_move(cell_2)

    # cell_3 = Cell(wdw, Point(100, 100), Point(150, 150))
    # cell_3.draw("black")
    # cell_2.draw_move(cell_3)

    # cell_4 = Cell(wdw, Point(150, 100), Point(200, 150))
    # cell_4.draw("black")
    # cell_3.draw_move(cell_4)

    # cell_5 = Cell(wdw, Point(150, 50), Point(200, 100))
    # cell_5.draw("black")
    # cell_4.draw_move(cell_5)

    # cell_6 = Cell(wdw, Point(50, 100), Point(100, 150))
    # cell_6.draw("black")
    # cell_1.draw_move(cell_6)

    # [1] draw lines:
    # ln_1 = Line(Point(50, 50), Point(550, 250))
    # wdw.draw_line(ln_1, "red")

    # ln_2 = Line(Point(400, 100), Point(700, 30))
    # wdw.draw_line(ln_2, "blue")

    # ln_3 = Line(Point(500, 500), Point(5, 5))
    # wdw.draw_line(ln_3, "green")

    # [2] draw cells:
    # cell_3 = Cell(wdw, Point(30, 80), Point(250, 250))
    # cell_3.has_right_wall = False
    # cell_3.draw("grey")

    # cell_4 = Cell(wdw, Point(25, 60), Point(100, 100))
    # cell_4.has_top_wall = False
    # cell_4.draw("magenta")

    wdw.wait_for_close()


main()
