class Board:
    def __init__(self, name: str, nrows: int, ncols: int, blank_char: str):
        self.name = name
        self.nrows = nrows
        self.ncols = ncols
        self.blank = blank_char

        self.array = [
            [blank_char for c in range(ncols)]
            for r in range(nrows)
        ]

    def __str__(self):
        output = self.name + "\n"

        output += "  "
        for c in range(self.ncols):
            output += str(c) + " "
        output += "\n"

        for r in range(self.nrows):
            output += str(r) + " "
            for c in range(self.ncols):
                x = self.array[r][c]
                output += x + " "
            output += "\n"

        return output.rstrip("\n")

    def __repr__(self):
        output = (
                "Board(" + self.name + ", " + self.blank +
                ", " + str(self.array) + ")"
        )
        return output

    def place_char(self, x: int, y:int , input_char: str) -> None:
        self.array[y][x] = input_char

    def clear_char(self, x: int, y: int)-> None:
        self.array[y][x] = self.blank

