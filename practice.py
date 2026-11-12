from utils import add_numbers, multiply_numbers, read_integer


def main() -> None:
    while True:
        while True:
            print("Izvēlies darbību:")
            print("1 - Saskaitīšana")
            print("2 - Reizināšana")
            operation = input("Tava izvēle: ")
            if operation in ("1", "2"):
                break
            print("Nederīga izvēle. Izvēlies 1 vai 2.")

        first = read_integer("Ievadi pirmo skaitli: ")
        second = read_integer("Ievadi otro skaitli: ")

        if operation == "1":
            print(f"Rezultāts: {add_numbers(first, second)}")
        else:
            print(f"Rezultāts: {multiply_numbers(first, second)}")

        while True:
            repeat = input("Vai vēlies veikt vēl vienu aprēķinu? (jā/nē): ").strip().lower()
            if repeat in ("j", "ja", "jā"):
                break
            if repeat in ("n", "ne", "nē"):
                return
            print("Lūdzu, atbildi ar jā vai nē.")


if __name__ == "__main__":
    main()
