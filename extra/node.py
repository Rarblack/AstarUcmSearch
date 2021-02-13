from statics import *
import pygame

class Node:
    def __init__(self, id, square_id, row, col):
        self.__id                   = id
        self.__square_id            = square_id
        self.__row                  = row
        self.__col                  = col
        self.__g_score              = float("inf")
        self.__f_score              = float("inf")
        self.__distance             = None
        self.__parent               = None
        self.__neighbors            = []

    def add_neighbor(self, neighbor):
        self.__neighbors.append(neighbor)

    def update__parent(self, node):
        self.__parent = node

    def update_g_score(self, g_score):
        self.__g_score = g_score

    def update_f_score(self, f_score):
        self.__f_score = f_score

    def set_distance(self, distance):
        self.__distance = distance

    def get_id(self):
        return self.__id

    def get_square_id(self):
        return self.__square_id

    def get_pos(self):
        return self.__row, self.__col

    def get_distance(self):
        return self.__distance

    def get_g_score(self):
        return self.__g_score

    def get_f_score(self):
        return self.__f_score

    def get_neighbors(self):
        return self.__neighbors

    def compare_nodes(self, other):
        return self.__id == other.get_id()

    def compare_positions(self, other):
        return self.__square_id == other.get_square_id()

    def __lt__(self, other):
        return False