#!/usr/bin/env python3

import unittest

class FixedMultiStack:
    # fixed capacity implementation

    def __init__(self, capacity, n_stacks=3):
        self.n_stacks = n_stacks
        self.capacity = capacity
        self.values = [None] * capacity * n_stacks
        self.indices = [-1] * n_stacks

    def __actual_index(self, index, stack_num):
        return index + stack_num * self.capacity

    def push(self, stack_num, value):
        index = self.indices[stack_num] + 1
        if  index + 1 > self.capacity:
            raise ValueError(f'stack {stack_num} is already full')

        self.values[self.__actual_index(index, stack_num)] = value
        self.indices[stack_num] += 1

    def pop(self, stack_num):
        index = self.indices[stack_num]
        if index < 0:
            return None

        value = self.values[self.__actual_index(index, stack_num)]
        self.indices[stack_num] -= 1
        return value

    def peek(self, stack_num):
        index = self.indices[stack_num]
        if index < 0:
            return None

        return self.values[self.__actual_index(index, stack_num)]

class Test(unittest.TestCase):

    def test(self):
        ms = FixedMultiStack(5)
        ms.push(0, 1)
        ms.push(0, 2)
        ms.push(0, 3)
        ms.push(1, 3)
        ms.push(2, 2)
        self.assertEqual(2, ms.pop(2))
        self.assertEqual(3, ms.pop(0))
        self.assertEqual(2, ms.pop(0))
        self.assertEqual(1, ms.pop(0))
        self.assertEqual(3, ms.pop(1))

        ms = FixedMultiStack(1)
        ms.push(0, 1)
        self.assertEqual(1, ms.peek(0))
        with self.assertRaises(ValueError):
            ms.push(0, 2)
        self.assertEqual(1, ms.pop(0))

if __name__ == "__main__":
    unittest.main()
