from window import Window, Line, Point


def main():
    wdw = Window(800, 600)

    ln_1 = Line(Point(50, 50), Point(550, 250))
    wdw.draw_line(ln_1, "red")

    ln_2 = Line(Point(400, 100), Point(700, 30))
    wdw.draw_line(ln_2, "blue")

    wdw.wait_for_close()


main()
