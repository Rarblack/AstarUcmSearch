import pygame
import math
from queue import PriorityQueue
from statics import *

WIDTH = HEIGHT = 1000
# WIN = pygame.display.set_mode((WIDTH, WIDTH))
# pygame.display.set_caption("A* Path Finding Algorithm")

class AStarSearch:
    def __init__(self):
        self.rows    = rows
        self.columns = columns
        self.run     = True
        self.started = False
        self.start   = None
        self.end     = None

    def h(self, type):

        def manhattan(node1, node2):
            x1, y1 = node1.get_pos()
            x2, y2 = node2.get_pos()
            return abs(x1 - x2) + abs(y1 - y2)
        
        if type == 'manhattan':
            return manhattan

        return Exception('Insufficient function call. Check your method name or arguments')


    def algorithm(self, start, end):
        count = 0
        open_set = PriorityQueue()
        start.update_g_score(0)
        start.update_f_score(h('manhattan')(start, end))
        open_set.put((0, count, start))

        open_set_hash = {start}

        while not open_set.empty():

            current = open_set.get()
            open_set_hash.remove(current)

            if current.compare_node == end:
                return True

            for neighbor in current.get_neighbors():
                temp_g_score = current.get_g_score() + neighbor.get_distance() 

                if temp_g_score < neighbor.g_score:
                    neighbor.update_parent(current)
                    neighbor.update_g_score(temp_g_score)
                    neighbor.update_f_score(sum(temp_g_score, h('manhattan')(neighbor, end)))

                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((neighbor.get_f_score(), count, neighbor))
                        open_set_hash.add(neighbor)

        return False

def reconstruct_path(end, draw):
    node = end
    while not node == None:
        node = node.origin
     
