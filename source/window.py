from pygame import display, draw
from statics import WHITE, GREY


class Window:
    def __init__(self, width, rows, square_size):
        self.width          = width
        self.rows           = rows
        self.square_size    = square_size
        self.win            = display.set_mode((width, width))

        self.create_window()
         

    def draw_grid_lines(self):
        for i in range(self.rows):
            draw.line(self.win, GREY, (0, i * self.square_size), (self.width, i * self.square_size))
            for j in range(self.rows):
                draw.line(self.win, GREY, (j * self.square_size, 0), (j * self.square_size, self.width))

    def create_window(self):
        self.win.fill(WHITE)
        self.draw_grid_lines()
        self.update()
    
    def update_square(self, node):
        draw.rect(self.win, node.color, (node.x, node.y, self.square_size, self.square_size))

    def set_title(self, title):
        display.set_caption(title)

    def update(self):
        self.draw_grid_lines()
        display.update()

    def reset(self):
        self.win.fill(WHITE)
        self.draw_grid_lines()
        self.update()