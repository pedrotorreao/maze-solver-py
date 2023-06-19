import tkinter as tk

# from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = tk.Tk()
        self.__root.title("Maze Solver")
        self.__canvas = tk.Canvas(
            self.__root, width=self.width, height=self.height, bg="white"
        )
        # self.__canvas.pack(anchor=tk.CENTER, expand=True)
        self.__canvas.pack(fill=tk.BOTH, expand=True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("... closing the window!")

    def close(self):
        self.__running = False
