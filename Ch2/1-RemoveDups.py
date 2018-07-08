#!/usr/bin/env python

import unittest

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_first(self, value):
        self.head = Node(value, self.head)

    def delete_first(self):
        deleted = self.head
        if deleted:
            self.head = deleted.next
            deleted.next = None
        return deleted

    # O(n) time, O(n) space
    def remove_dups(self):
        if self.head == None:
            return

        value_map = {self.head.value : True}

        prev = self.head
        current = self.head.next
        while current:
            if current.value in value_map:
                # remove current node
                prev.next = current.next
                current.next = None
                current = prev.next
            else:
                value_map[current.value] = True
                prev = current
                current = current.next

class Test(unittest.TestCase):

    def test(self):
        ll = LinkedList(Node(1))
        ll.insert_first(2)
        ll.insert_first(3)
        ll.insert_first(4)
        ll.insert_first(2)
        ll.insert_first(2)
        ll.insert_first(3)
        ll.remove_dups()

        self.assertEquals(3, ll.delete_first().value)
        self.assertEquals(2, ll.delete_first().value)
        self.assertEquals(4, ll.delete_first().value)
        self.assertEquals(1, ll.delete_first().value)
        self.assertEquals(None, ll.delete_first())

        ll.insert_first(10)
        ll.insert_first(11)
        ll.remove_dups()

        self.assertEquals(11, ll.delete_first().value)
        self.assertEquals(10, ll.delete_first().value)
        self.assertEquals(None, ll.delete_first())

        ll = LinkedList(None)
        ll.remove_dups()

        self.assertEquals(None, ll.delete_first())

if __name__ == "__main__":
    unittest.main()
