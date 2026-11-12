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


def main() -> None:
    first = read_integer("Ievadi pirmo skaitli: ")
    second = read_integer("Ievadi otro skaitli: ")
    print(f"Summa: {add_numbers(first, second)}")


if __name__ == "__main__":
    main()
