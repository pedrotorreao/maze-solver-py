import tkinter as tk
from point import Point
from line import Line


class Cell:
    # constructor:
    def __init__(self, wndw=None, p1=None, p2=None):
        # cell coordinates in the canvas:
        self._p1 = p1  # top-left corner
        self._p2 = p2  # bottom-right corner
        # window container:
        self._wndw = wndw
        # by default, let us consider all the walls as existing:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    # draw the cell:
    def draw(self, fill_color="black"):
        if self._wndw is None:
            return
        # if the cell has a left wall, draw it:
        if self.has_left_wall:
            left_wall = Line(
                Point(self._p1.x, self._p1.y), Point(self._p1.x, self._p2.y)
            )
            self._wndw.draw_line(left_wall, fill_color)

        # if the cell has a right wall, draw it:
        if self.has_right_wall:
            right_wall = Line(
                Point(self._p2.x, self._p1.y), Point(self._p2.x, self._p2.y)
            )
            self._wndw.draw_line(right_wall, fill_color)

        # if the cell has a top wall, draw it:
        if self.has_top_wall:
            top_wall = Line(
                Point(self._p1.x, self._p1.y), Point(self._p2.x, self._p1.y)
            )
            self._wndw.draw_line(top_wall, fill_color)

        # if the cell has a bottom wall, draw it:
        if self.has_bottom_wall:
            bottom_wall = Line(
                Point(self._p1.x, self._p2.y), Point(self._p2.x, self._p2.y)
            )
            self._wndw.draw_line(bottom_wall, fill_color)

    def draw_move(self, to_cell, undo=False):
        # calculate starting cell center:
        start_center_x = self._p1.x + float((self._p2.x - self._p1.x) / 2.0)
        start_center_y = self._p1.y + float((self._p2.y - self._p1.y) / 2.0)

        # calculate ending cell center:
        end_center_x = to_cell._p1.x + float((to_cell._p2.x - to_cell._p1.x) / 2)
        end_center_y = to_cell._p1.y + float((to_cell._p2.y - to_cell._p1.y) / 2)

        fill_color = "red"
        if undo:
            fill_color = "grey"

        # move from LEFT to RIGHT:
        if self._p1.x > to_cell._p1.x:
            # center_1 --> left_wall_1:
            ln_1 = Line(
                Point(start_center_x, start_center_y),
                Point(self._p1.x, start_center_y),
            )
            self._wndw.draw_line(ln_1, fill_color)
            # right_wall_2 --> center_2:
            ln_2 = Line(
                Point(to_cell._p2.x, end_center_y), Point(end_center_x, end_center_y)
            )
            self._wndw.draw_line(ln_2, fill_color)

        # move from RIGHT to LEFT:
        elif self._p1.x < to_cell._p1.x:
            # center_1 --> right_wall_1:
            ln_1 = Line(
                Point(start_center_x, start_center_y), Point(self._p2.x, start_center_y)
            )
            self._wndw.draw_line(ln_1, fill_color)
            # left_wall_2 --> center_2:
            ln_2 = Line(
                Point(to_cell._p1.x, end_center_y), Point(end_center_x, end_center_y)
            )
            self._wndw.draw_line(ln_2, fill_color)

        # move from TOP to BOTTOM:
        elif self._p1.y > to_cell._p1.y:
            # center_1 --> top_wall_1:
            ln_1 = Line(
                Point(start_center_x, start_center_y), Point(start_center_x, self._p1.y)
            )
            self._wndw.draw_line(ln_1, fill_color)
            # bottom_wall_2 --> center_2:
            ln_2 = Line(
                Point(end_center_x, to_cell._p2.y), Point(end_center_x, end_center_y)
            )
            self._wndw.draw_line(ln_2, fill_color)

        # move from BOTTOM to TOP:
        elif self._p1.y < to_cell._p1.y:
            # center_1 --> bottom_wall_1:
            ln_1 = Line(
                Point(start_center_x, start_center_y), Point(start_center_x, self._p2.y)
            )
            self._wndw.draw_line(ln_1, fill_color)
            # top_wall_2 --> center_2:
            ln_2 = Line(
                Point(end_center_x, to_cell._p1.y), Point(end_center_x, end_center_y)
            )
            self._wndw.draw_line(ln_2, fill_color)
