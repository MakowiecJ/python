class Node:
    def __init__(self):
        self.words = []
        self.nodes = [None] * 8
        self.node_dict = {'b2': self.nodes[0], 'b3': self.nodes[1], 'b4': self.nodes[2], 'b5': self.nodes[3], 'b6': self.nodes[4], 'b7': self.nodes[5], 'b8': self.nodes[6], 'b9': self.nodes[7]}