from utils import add_numbers, read_integer


def main() -> None:
    first = read_integer("Ievadi pirmo skaitli: ")
    second = read_integer("Ievadi otro skaitli: ")
    print(f"Summa: {add_numbers(first, second)}")


if __name__ == "__main__":
    main()
