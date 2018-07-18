#!/usr/bin/env python3

import unittest

class Node:

    def __init__(self, name, adjacent):
        self.name = name
        self.adjacent = adjacent
        self.marked = False

# BFS solution
# TODO: check if answer is true
def hasRoot(node1, node2):
    queue = [node1]
    node1.marked = True

    while len(queue) > 0:
        node = queue.pop(0)
        if node.name == node2.name:
            return True
        if not node.marked:
            node.marked = True
            queue.append(node.adjacent)

class Test(unittest.TestCase):

    def test(self):
        # TODO: write test
        pass

if __name__ == "__main__":
    unittest.main()
