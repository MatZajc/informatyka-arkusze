def zad4_2():
    with open("liczby_przyklad.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        first_line_numbers = sorted(
            [int(x) for x in lines[0].strip("\n\r").split(" ")])[::-1]

    print(first_line_numbers[100])


if (__name__ == "__main__"):
    zad4_2()
