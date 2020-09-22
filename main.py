from BoardPrinterProject.src.boards_manager import BoardManager


def main():
    man = BoardManager()
    man.create_board()
    print(man.active)

    while True:
        result = man.list_of_actions()
        print(man.active)
        if result == "DESTROY":
            del man
            break


if __name__ == "__main__":
    main()
