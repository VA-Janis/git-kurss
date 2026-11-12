from utils import add_numbers, ask_to_repeat, multiply_numbers, read_integer, select_operation


def main() -> None:
    while True:
        operation = select_operation()

        first = read_integer("Ievadi pirmo skaitli: ")
        second = read_integer("Ievadi otro skaitli: ")

        if operation == "1":
            print(f"Rezultāts: {add_numbers(first, second)}")
        else:
            print(f"Rezultāts: {multiply_numbers(first, second)}")

        if not ask_to_repeat():
            return


if __name__ == "__main__":
    main()
