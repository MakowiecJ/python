from nodes import Node


class T9:
    def __init__(self, words):
        self.root = Node()
        with open(words, 'r') as f:
            for word in f:
                word = word.lower().strip()
                self.insert(self.root, word, 0)
        print("Loaded dictionary")

    def get_root(self):
        return self.root

    def insert(self, node, word, index):
        if index == len(word) and node is not None:
            node.words.append(word)
            return

        c = word[index]
        if c in 'abc':
            if node.node_dict['b2'] is None:
                node.node_dict['b2'] = Node()
            node = node.node_dict['b2']
            self.insert(node, word, index + 1)
        elif c in 'def':
            if node.node_dict['b3'] is None:
                node.node_dict['b3'] = Node()
            node = node.node_dict['b3']
            self.insert(node, word, index + 1)
        elif c in 'ghi':
            if node.node_dict['b4'] is None:
                node.node_dict['b4'] = Node()
            node = node.node_dict['b4']
            self.insert(node, word, index + 1)
        elif c in 'jkl':
            if node.node_dict['b5'] is None:
                node.node_dict['b5'] = Node()
            node = node.node_dict['b5']
            self.insert(node, word, index + 1)
        elif c in 'mno':
            if node.node_dict['b6'] is None:
                node.node_dict['b6'] = Node()
            node = node.node_dict['b6']
            self.insert(node, word, index + 1)
        elif c in 'pqrs':
            if node.node_dict['b7'] is None:
                node.node_dict['b7'] = Node()
            node = node.node_dict['b7']
            self.insert(node, word, index + 1)
        elif c in 'tuv':
            if node.node_dict['b8'] is None:
                node.node_dict['b8'] = Node()
            node = node.node_dict['b8']
            self.insert(node, word, index + 1)
        elif c in 'wxyz':
            if node.node_dict['b9'] is None:
                node.node_dict['b9'] = Node()
            node = node.node_dict['b9']
            self.insert(node, word, index + 1)
        else:
            print("Insertion Error")
            print(f"word: {word} index: {index}")
