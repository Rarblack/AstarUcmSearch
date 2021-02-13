from queue import PriorityQueue
from statics import *
from node import Node
from window import Window
import pygame
import helpers


class Main:
    def __init__(self, width, rows):
        self.width          = width
        self.rows           = rows
        self.type           = 1

        self.start          = None
        self.end            = None

        self.square_size    = self.calculate_square_size(width, rows)
        self.grid           = self.create_grid()
        
        self.window = Window(self.width, self.rows, self.square_size)
        self.window.set_title('A*')

    def create_grid(self):
        return [[Node(i, j, self.square_size, self.rows) for j in range(self.rows)] for i in range(self.rows)]

    def calculate_square_size(self, width, rows):
        return width // rows      

    def algorithm(self):
        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, self.start))
        self.start.update_g_score(0)
        self.start.update_f_score(helpers.h(self.start.get_pos(), self.end.get_pos()) if self.type else 0)

        open_set_hash = {self.start}

        while not open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == self.end:
                return True

            for neighbor in current.neighbors:
                temp_g_score = current.g_score + 1

                if temp_g_score < neighbor.g_score:
                    neighbor.update_parent(current)
                    neighbor.update_g_score(temp_g_score)
                    neighbor.update_f_score(temp_g_score + helpers.h(neighbor.get_pos(), self.end.get_pos()) if self.type else 0)

                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((neighbor.f_score, count, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_open()
                        
            if current != self.start:
                current.make_closed()

            # below code reflects the changes on the graph    
            self.window.update_square(current)
            for neighbor in current.neighbors:
                self.window.update_square(neighbor)
            self.window.update()

        return False

    def get_shortest_path(self):
        self.end.make_end()
        self.window.update_square(self.end)
        current = self.end
        while current.parent.parent:
            current = current.parent
            current.make_path()

            pygame.time.wait(10)
            self.window.update_square(current)
            self.window.update()
    def run(self):
    
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:   # LEFT CLICK or RIGHT CLICK
                    pos = pygame.mouse.get_pos()
                    row, col = helpers.convert_pos(pos, self.square_size)
                    node = self.grid[row][col]
                    
                    if pygame.mouse.get_pressed()[0]:
                        if not self.start:
                            self.start = node
                            self.start.make_start()

                        elif not self.end:
                            self.end = node
                            self.end.make_end()

                        elif node != self.end and node != self.start:
                            node.make_barrier()
                    else:
                        node.reset()
                        if node == self.start:
                            self.start = None
                        elif node == self.end:
                            self.end = None

                    self.window.update_square(node)
                    self.window.update()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.start and self.end:
                        for row in self.grid:
                            for node in row:
                                node.update_neighbors(self.grid)
                        
                        if self.algorithm():
                            self.get_shortest_path()
                        

                    if event.key == pygame.K_c:
                        self.start   = None
                        self.end     = None
                        self.grid    = self.create_grid()
                        self.window.reset()

                    # switch from a* to ucm and ucm to a* (by default it is a*)
                    if event.key == pygame.K_s:
                        self.type = not self.type
                        self.window.set_title('A*' if self.type else 'UCM')

        pygame.quit()


main = Main(WIDTH, ROWS)
main.run()