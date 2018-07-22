#!/usr/bin/env python3

import unittest

class Node:

    def __init__(self, name):
        self.name = name
        self.adjacent = list()
        self.marked = False

    def __repr__(self):
        return f"{self.name}, {self.adjacent}"

    def add(self, node):
        if self.adjacent == None:
            self.adjacent = [node]
        else:
            self.adjacent.append(node)

# BFS solution
def BFS(node1, node2):
    queue = [node1]

    while len(queue) > 0:
        node = queue.pop(0)
        print(node.name)
        if node.name == node2.name:
            return True
        if not node.marked:
            node.marked = True
            for adj in node.adjacent:
                queue.append(adj)
    return False

def hasRoute(node1, node2):
    if BFS(node1, node2):
        return True
    if BFS(node2, node1):
        return True

class Test(unittest.TestCase):

    def test1(self):
        node1 = Node("1")
        node2 = Node("2")
        node3 = Node("3")
        node4 = Node("4")
        node1.add(node2)
        node1.add(node3)
        node2.add(node3)
        node2.add(node4)
        node4.add(node3)
        self.assertTrue(hasRoute(node1, node4))

    def test2(self):
        node1 = Node("1")
        node2 = Node("2")
        node3 = Node("3")
        node4 = Node("4")
        node5 = Node("5")
        node1.add(node2)
        node2.add(node3)
        node2.add(node4)
        node3.add(node4)
        node3.add(node5)
        self.assertTrue(hasRoute(node1, node5))

    def test3(self):
        print("test3")
        node1 = Node("1")
        node2 = Node("2")
        node3 = Node("3")
        node4 = Node("4")
        node5 = Node("5")
        node1.add(node2)
        node2.add(node3)
        node2.add(node4)
        node3.add(node4)
        self.assertFalse(hasRoute(node1, node5))

if __name__ == "__main__":
    unittest.main()
