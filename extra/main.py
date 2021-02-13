import pygame
import math
from queue import PriorityQueue
from statics import *
from custom_parser import Parser
from node import Node

class Main:
   def __init__(self):
      self.__nodes         = []

      self.__parser        = None
      self.__filename      = None
      self.__search_type   = None


   def create_nodes(self, nodes):
      try:
         if self.__nodes:
            raise
         for nodeID, squareID in nodes: 
            row = squareID // 10
            col = squareID %  10

            self.__nodes.append(Node(nodeID, squareID, row, col))
      
      except:
         print('Nodes have already been created', end='\n')

   def update_nodes(self, edges):
         for _from, to, distance in edges:
            from_node = self.__nodes[_from]
            to_node   = self.__nodes[to]
            from_node.add_neighbor(to_node)
            to_node.add_neighbor(from_node)

            if from_node.compare_positions(to_node):
               self.__nodes[_from].set_distance(14.1)
               self.__nodes[to].set_distance(14.1)
            else:
               self.__nodes[_from].set_distance(distance)
               self.__nodes[to].set_distance(distance)

   def parse(self, search_type, filename, file_location=''):
      try:
         if self.__parser and self.__filename == filename:
            raise

         self.__search_type   = search_type
         self.__filename      = filename
         self.__parser        = Parser(search_type, filename, file_location)
         
         return self.__parser

      except:
         print('You have already parsed the same file. The request has not been accepted. Previously parsed data is returned', end='\n')
         return self.__parser


   def run(self):
      pass


main     = Main()
parser   = main.parse('astar', 'p1_graph.txt')
main.create_nodes(parser.get_nodes())
main.update_nodes(parser.get_edges())
