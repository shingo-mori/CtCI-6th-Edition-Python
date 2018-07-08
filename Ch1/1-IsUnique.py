#!/usr/bin/env python

import unittest

# O(n)
def is_unique(string):
    char_flag = 0
    for c in string:
        code = ord(c)
        if char_flag & (1 << code):
            return False
        char_flag |= (1 << code)
    return True

class Test(unittest.TestCase):

    def test(self):
        uniques = [\
                "a",
                "ab",
                "",
                "abcdefg,hIjKlmn",
                "abcxyz",
                ]
        non_uniques = [
                "Hello, World!",
                "aa"
                "abcdefa"
                ]

        for unique in uniques:
            self.assertEqual(True, is_unique(unique), unique)
        for non_unique in non_uniques:
            self.assertEqual(False, is_unique(non_unique), non_unique)

if __name__ == "__main__":
    unittest.main()
