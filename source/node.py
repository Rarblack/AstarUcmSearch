from statics import *


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row        = row
        self.col        = col
        self.x          = row * width
        self.y          = col * width
        self.color      = WHITE
        self.neighbors  = []
        self.width      = width
        self.total_rows = total_rows

        self.g_score    = float("inf")
        self.f_score    = float("inf")
        self.parent     = None

    def update_g_score(self, g_score):
        self.g_score = g_score

    def update_f_score(self, f_score):
        self.f_score = f_score
    
    def update_parent(self, parent):
        self.parent = parent

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def update_neighbors(self, grid):
        self.neighbors = []

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])
        

    def __lt__(self, other):
        return False
        # return self.f_score < other.f_score