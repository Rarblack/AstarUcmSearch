def convert_pos(pos, square_size):
    return list(map(lambda x: x // square_size, pos))

# manhattan heuristic
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)  