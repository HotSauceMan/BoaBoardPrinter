import unittest

from BoardPrinterProject.src.board import Board


class TestBoard(unittest.TestCase):
    def test_place_and_clear_char(self):
        a = Board("Bob", 2, 2, "x")
        # array = a.array.copy()
        a.place_char(1, 1, "A")
        self.assertEqual("A", a.array[1][1]) # place char

        a.clear_char(1, 1)
        self.assertEqual("x", a.array[1][1])
    def test_place_and_clear_char2(self):
        a = Board("Bob", 3, 3, "a")
        # array = a.array.copy()
        a.place_char(2, 2, "b")
        self.assertEqual("b", a.array[2][2]) # place char

        a.clear_char(1, 1)
        self.assertEqual("a", a.array[1][1])

if __name__ == '__main__':
    unittest.main()
