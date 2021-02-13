
class Parser:
    def __init__(self, search_type, filename, file_location):
        self.__filename           = filename.strip()
        self.__search_type        = search_type.strip().lower()
        self.__file_location      = file_location.strip()
        self.__nodes              = [] # vertex ID, square ID
        self.__edges              = [] # from, to, distance
        self.__start              = None
        self.__end                = None

        self.__parse()

    def __parse(self):
        if self.__search_type == 'astar' or self.__search_type == 'ucm':
            self.__parse_astar_ucm_file()
        
    def __parse_astar_ucm_file(self):  
        switch = 0

        with open(self.__filename) as file:
            for line in file.readlines():
                data = line.strip("\n").split(",")

                try:
                    if switch == 0:
                        self.__nodes.append(list(map(int, data)))
                    elif switch == 1:
                        self.__edges.append(list(map(int, data)))
                    else:
                        if data[0].lower() == 's':
                            self.__start = int(data[1])
                        elif data[0].lower() == 'd':
                            self.__end   = int(data[1])
                except:
                    if not list(filter(lambda x: x != '', data)): # remove all empty strings, if remaining list is empty then we just hit the empty line
                        switch += 1


    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end       
    
    def get_nodes(self):
        return self.__nodes

    def get_edges(self):
        return self.__edges

    def get_full_file_path(self):
        return self.__file_location.strip().rstrip('/') + '/' + self.__filename.strip()
