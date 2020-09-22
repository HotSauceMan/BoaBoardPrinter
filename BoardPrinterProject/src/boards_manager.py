from BoardPrinterProject.src.board import Board


class BoardManager():
    def __init__(self)-> None:
        self.collection = []
        self.active = None

    def create_board(self)-> None:
        name = input("Enter the name of your board: ")
        nrows = int(input("Enter the number of rows for your board: "))
        ncols = int(input("Enter the number of columns for your board: "))
        blank_char = input(
            "Enter the blank character to be used on your board: ")

        board = Board(name, nrows, ncols, blank_char)

        self.collection = [board] + self.collection

        if self.active is None:
            self.active = self.collection[0]

    def list_of_actions(self)-> None: # type: ignore
        action = {
            "1": "Fill Spot",
            "2": "Erase Spot",
            "3": "Switch Board",
            "4": "Create Board",
            "5": "Quit"
        }

        print("Select your action from the list below.")
        for (k, v) in sorted(action.items()):
            print(f'{k}. {v}')
        print()
        while True:
            inp = input(
                "Enter the number of the action you would like to do: ")

            if inp in action:
                break

        if inp == "1":
            self.place_char_on()
        elif inp == "2":
            self.clear_char_on()
        elif inp == "3":
            self.switch_board()
        elif inp == "4":
            self.create_board()
        elif inp == "5":
            return self.terminate()

    def switch_board(self)-> None: # type: None
        for (i, board) in enumerate(self.collection):
            print(f'{i}. {board.name}')

        while True:
            inp = input("Enter the number of the board you want to switch to: ")

            try:
                int_inp = int(inp)
                if int_inp in range(len(self.collection)):
                    break
            except ValueError:  # we know it's a ValueError
                pass

        self.active = self.collection[int_inp]

    def place_char_on(self)-> None:  # type: str
        character = input("Enter the character you would like to add on the board: ")
        while True:
            position = input("Enter the position to place the character in the form row,col: ")
            (row, col) = position.split(",")

            if row.isnumeric() and col.isnumeric():
                break

        self.active.place_char(int(col), int(row), character)

    def clear_char_on(self)-> None: # type: str
        while True:
            position = input("Enter the position to place the character in the form row,col: ")
            (row, col) = position.split(",")

            if row.isnumeric() and col.isnumeric():
                break

        self.active.clear_char(int(col), int(row))

    def terminate(self)-> None: # type: str
        return "DESTROY"
