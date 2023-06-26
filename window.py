import tkinter as tk
from point import Point
from line import Line
from cell import Cell


class Window:
    # constructor:
    def __init__(self, width, height):
        # canvas dimensions:
        self.width = width
        self.height = height
        # create the root window/container :
        self._root = tk.Tk()
        self._root.title("Maze Solver")
        # create a canvas widget inside the root window:
        self._canvas = tk.Canvas(
            self._root, width=self.width, height=self.height, bg="white"
        )
        # allocate all the space available in the window for the canvas and
        # make the canvas fill it along both axis:
        self._canvas.pack(fill=tk.BOTH, expand=True)
        # boolean that indicates whether the window is being used:
        self._running = False
        # connect the close() method to the "delete window" action:
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    # redraw all the graphics in the window:
    def redraw(self):
        # process those events which are not running or stable:
        self._root.update_idletasks()
        # process all the events present in the application:
        self._root.update()

    # keep the window running until it is closed:
    def wait_for_close(self):
        # update window running state:
        self._running = True
        while self._running:
            self.redraw()
        print("... closing the window!")

    # stop program from running when window is closed:
    def close(self):
        # update window running state:
        self._running = False

    # take an instance of a Line and a fill_color as inputs, then call the
    # Line's draw() method:
    def draw_line(self, line, fill_color="red"):
        line.draw(self._canvas, fill_color)
