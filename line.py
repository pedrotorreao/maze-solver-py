import tkinter as tk
from point import Point


class Line:
    # constructor:
    def __init__(self, p1, p2):
        self._p1 = p1  # start Point
        self._p2 = p2  # end Point

    # take a 'canvas' and a 'fill color' and draw a line by calling the Canva's
    # 'create_line' method:
    def draw(self, cnv, fill_color):
        cnv.create_line(
            self._p1.x, self._p1.y, self._p2.x, self._p2.y, fill=fill_color, width=2
        )
        cnv.pack(fill=tk.BOTH, expand=1)
