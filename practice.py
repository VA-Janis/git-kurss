def add_numbers(first: int, second: int) -> int:
    return first + second


def main() -> None:
    first = int(input("Ievadi pirmo skaitli: "))
    second = int(input("Ievadi otro skaitli: "))
    print(f"Summa: {add_numbers(first, second)}")


if __name__ == "__main__":
    main()
