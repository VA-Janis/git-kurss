def add_numbers(first: int, second: int) -> int:
    return first + second


def multiply_numbers(first: int, second: int) -> int:
    return first * second


def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Lūdzu, ievadi veselu skaitli.")


def select_operation() -> str:
    while True:
        print("Izvēlies darbību:")
        print("1 - Saskaitīšana")
        print("2 - Reizināšana")
        operation = input("Tava izvēle: ")
        if operation in ("1", "2"):
            return operation
        print("Nederīga izvēle. Izvēlies 1 vai 2.")
