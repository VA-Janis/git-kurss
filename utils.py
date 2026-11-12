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
