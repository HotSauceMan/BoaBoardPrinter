import unittest
from unittest.mock import patch

from BoardPrinterProject.src.boards_manager import BoardManager
from BoardPrinterProject.src.board import Board


class TestBoardManager(unittest.TestCase):
    def test_create_board(self):
        name = "Bob"
        rows = 2
        cols = 2
        blank_char = "x"

        a = BoardManager()  # create a Board() through .create_board() method
        b = Board(name, rows, cols, blank_char)  # create an identical Board() directly from Board() class

        inputs = [name, str(rows), str(cols), blank_char]
        target = "BoardPrinterProject.src.boards_manager.input"
        with patch(target, side_effect=inputs):
            # whatever is in this block, if call for input, iterate through inputs list
            a.create_board()

            self.assertEqual(a.active, a.collection[0])
            self.assertEqual(repr(a.active), repr(b))

    def test_switch_board(self):
        man = BoardManager()

        inputs = ["A", 1, 1, "*"]
        target = "BoardPrinterProject.src.boards_manager.input"
        with patch(target, side_effect=inputs):
            man.create_board()
            self.assertEquals(man.active, man.collection[0])

        inputs = ["B", 1, 1, "*"]
        with patch(target, side_effect=inputs):
            man.create_board()
            self.assertEquals(man.active, man.collection[1])

        inputs = ["0"]
        with patch(target, side_effect=inputs):
            man.switch_board()
            self.assertEquals(man.active, man.collection[0])


if __name__ == '__main__':
    unittest.main()
