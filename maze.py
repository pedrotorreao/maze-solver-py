import time
from cell import Cell
from point import Point


class Maze:
    # constructor:
    def __init__(self, p, num_rows, num_cols, cell_sz_x, cell_sz_y, wndw=None):
        # coordinates for the top-left corner:
        self._p = p
        # window container:
        self._wndw = wndw
        # 2d list - grid:
        self._cells = []
        # number of rows and cells to be drawn to the grid:
        self._num_rows = num_rows
        self._num_cols = num_cols
        # x/y dimensions each cell:
        self._cell_sz_x = cell_sz_x
        self._cell_sz_y = cell_sz_y

        # build the grid:
        self._create_cells()

    # populate the 2d grid with Cell objects:
    def _create_cells(self):
        for c in range(0, self._num_cols):
            # new cell coordinate in the y-axis:
            new_y1 = self._p.y + c * self._cell_sz_y
            # column list to be filled:
            column = []
            for r in range(0, self._num_rows):
                # new cell coordinate in the x-axis:
                new_x1 = self._p.x + r * self._cell_sz_x

                # calculate/create start and end coordinates for the new cell:
                start = Point(new_x1, new_y1)
                end = Point(new_x1 + self._cell_sz_x, new_y1 + self._cell_sz_y)

                # create a new Cell object:
                new_cell = Cell(self._wndw, start, end)
                # append new cell to the column list:
                column.append(new_cell)
            # add the recently filled column to the grid:
            self._cells.append(column)
        # ready for drawing the grid:
        self._draw_cells()

    # go over the grid drawinf each cell:
    def _draw_cells(self):
        if self._wndw is None:
            return
        for r in range(0, self._num_rows):
            for c in range(0, self._num_cols):
                self._cells[r][c].draw()
                self._animate()

    # slow down the drawing to allow the user to visualize it:
    def _animate(self):
        if self._wndw is None:
            return
        self._wndw.redraw()
        time.sleep(0.05)
