import time
import random

from cell import Cell
from point import Point


class Maze:
    # constructor:
    def __init__(
        self, p, num_rows, num_cols, cell_sz_x, cell_sz_y, wndw=None, seed=None
    ):
        # coordinates for the top-left corner:
        self._p = p
        # window container:
        self._wndw = wndw
        # seed for random creation:
        self._seed = seed
        # 2d list - grid:
        self._cells = []
        # number of rows and cells to be drawn to the grid:
        self._num_rows = num_rows
        self._num_cols = num_cols
        # x/y dimensions each cell:
        self._cell_sz_x = cell_sz_x
        self._cell_sz_y = cell_sz_y
        # seeding the randomness to vary the wall selection:
        if seed is not None:
            seed = random.seed(seed)

        # build the grid:
        self._create_cells()

        # open entry and exit walls:
        self._break_entrance_and_exit()

        # break walls for traversing the maze:
        self._break_walls_recursively(0, 0)

        # reset the visited property of all the cells:
        self._reset_cells_visited()

    # populate the 2d grid with Cell objects:
    def _create_cells(self):
        for r in range(0, self._num_rows):
            # new cell coordinate in the x-axis:
            new_x1 = self._p.x + r * self._cell_sz_x
            # column list to be filled:
            column = []
            for c in range(0, self._num_cols):
                # new cell coordinate in the y-axis:
                new_y1 = self._p.y + c * self._cell_sz_y

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

    # go over the grid drawing each cell:
    def _draw_cells(self, i=None, j=None):
        if self._wndw is None:
            return

        if (i is not None) and (j is not None):
            self._cells[i][j].draw()
            self._animate()
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
        time.sleep(0.025)

    # break down walls for entry and exit paths:
    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        top_left_cell.has_top_wall = False
        self._draw_cells(0, 0)

        bottom_right_cell = self._cells[self._num_rows - 1][self._num_cols - 1]
        bottom_right_cell.has_bottom_wall = False
        self._draw_cells(self._num_rows - 1, self._num_cols - 1)

    # break walls to find path:
    def _break_walls_recursively(self, i, j):
        # mark current cell as visited:
        self._cells[i][j]._visited = True

        while True:
            # list containing all possible directions [i±1,j±1] to move from
            # current cell, [i,j]:
            adjacent_cells = []
            # store the amount of possible directions from current cell:
            directions_counter = 0

            # check if it's possible to move left:
            if (i > 0) and (not self._cells[i - 1][j]._visited):
                adjacent_cells.append((i - 1, j))
                directions_counter += 1
            # check if it's possible to move right:
            if (i < self._num_rows - 1) and (not self._cells[i + 1][j]._visited):
                adjacent_cells.append((i + 1, j))
                directions_counter += 1
            # check if it's possible to move up:
            if (j > 0) and (not self._cells[i][j - 1]._visited):
                adjacent_cells.append((i, j - 1))
                directions_counter += 1
            # check if it's possible to move down:
            if (j < self._num_cols - 1) and (not self._cells[i][j + 1]._visited):
                adjacent_cells.append((i, j + 1))
                directions_counter += 1

            # if there were no possible paths to follow, break out of the loop:
            if directions_counter == 0:
                self._draw_cells(i, j)
                return

            # otherwise, select a random direction to go from the current cell:
            moving_to = adjacent_cells[random.randrange(directions_counter)]

            # now, we remove the walls blocking the path from the current
            # cell to the cell we are moving to:
            # if moving left:
            if moving_to[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # if moving right:
            if moving_to[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # if moving up:
            if moving_to[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            # if moving down:
            if moving_to[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            # explore the next cell:
            self._break_walls_recursively(moving_to[0], moving_to[1])

    # reset the 'visited' property of all the cells in the maze to False:
    def _reset_cells_visited(self):
        for r in range(0, self._num_rows):
            for c in range(0, self._num_cols):
                self._cells[r][c]._visited = False

    # solve maze using a depth-first recursive approach:
    def _solve_dfs_r(self, i, j):
        self._animate()

        # mark current cell as visited:
        self._cells[i][j]._visited = True

        # if arrived at the exit of the maze, return True:
        if (i == self._num_rows - 1) and (j == self._num_cols - 1):
            return True

        # move UP:
        if (
            (i > 0)
            and (not self._cells[i - 1][j]._visited)
            and (not self._cells[i][j].has_left_wall)
        ):
            move_from = self._cells[i][j]
            move_to = self._cells[i - 1][j]

            move_from.draw_move(move_to)

            valid_move = self._solve_dfs_r(i - 1, j)

            if valid_move:
                return True
            else:
                move_from.draw_move(move_to, True)

        # move RIGHT:
        if (
            (j < self._num_cols - 1)
            and (not self._cells[i][j + 1]._visited)
            and (not self._cells[i][j].has_bottom_wall)
        ):
            move_from = self._cells[i][j]
            move_to = self._cells[i][j + 1]

            move_from.draw_move(move_to)

            valid_move = self._solve_dfs_r(i, j + 1)

            if valid_move:
                return True
            else:
                move_from.draw_move(move_to, True)

        # move DOWN:
        if (
            (i < self._num_rows - 1)
            and (not self._cells[i + 1][j]._visited)
            and (not self._cells[i][j].has_right_wall)
        ):
            move_from = self._cells[i][j]
            move_to = self._cells[i + 1][j]

            move_from.draw_move(move_to)

            valid_move = self._solve_dfs_r(i + 1, j)

            if valid_move:
                return True
            else:
                move_from.draw_move(move_to, True)

        # move LEFT:
        if (
            (j > 0)
            and (not self._cells[i][j - 1]._visited)
            and (not self._cells[i][j].has_top_wall)
        ):
            move_from = self._cells[i][j]
            move_to = self._cells[i][j - 1]

            move_from.draw_move(move_to)

            valid_move = self._solve_dfs_r(i, j - 1)

            if valid_move:
                return True
            else:
                move_from.draw_move(move_to, True)

        return False

    # solve maze caller:
    def solve(self):
        return self._solve_dfs_r(0, 0)
