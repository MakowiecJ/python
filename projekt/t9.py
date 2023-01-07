from nodes import Node


class T9:
    def __init__(self):
        self.root = Node()
        with open('english.txt', 'r') as f:
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
            if node.nodes[0] is None:
                node.nodes[0] = Node()
            node = node.nodes[0]
            self.insert(node, word, index + 1)
        elif c in 'def':
            if node.nodes[1] is None:
                node.nodes[1] = Node()
            node = node.nodes[1]
            self.insert(node, word, index + 1)
        elif c in 'ghi':
            if node.nodes[2] is None:
                node.nodes[2] = Node()
            node = node.nodes[2]
            self.insert(node, word, index + 1)
        elif c in 'jkl':
            if node.nodes[3] is None:
                node.nodes[3] = Node()
            node = node.nodes[3]
            self.insert(node, word, index + 1)
        elif c in 'mno':
            if node.nodes[4] is None:
                node.nodes[4] = Node()
            node = node.nodes[4]
            self.insert(node, word, index + 1)
        elif c in 'pqrs':
            if node.nodes[5] is None:
                node.nodes[5] = Node()
            node = node.nodes[5]
            self.insert(node, word, index + 1)
        elif c in 'tuv':
            if node.nodes[6] is None:
                node.nodes[6] = Node()
            node = node.nodes[6]
            self.insert(node, word, index + 1)
        elif c in 'wxyz':
            if node.nodes[7] is None:
                node.nodes[7] = Node()
            node = node.nodes[7]
            self.insert(node, word, index + 1)
        else:
            print("Insertion Error")
            print(f"word: {word} index: {index}")

    def getRoot(self):
        return self.root
