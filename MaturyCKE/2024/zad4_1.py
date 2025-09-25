def zad4_1():
    first_number_dividers_count = 0
    with open("liczby_przyklad.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        first_line_numbers = [int(x)
                              for x in lines[0].strip("\n\r").split(" ")]
        second_line_numbers = [int(x)
                               for x in lines[1].strip("\n\r").split(" ")]

        for first_number in first_line_numbers:
            first_number_dividers = len(list(filter(
                lambda second_number: second_number % first_number == 0, second_line_numbers)))
            if (first_number_dividers > 0):
                first_number_dividers_count += 1
        print(first_number_dividers_count)


if (__name__ == "__main__"):
    zad4_1()
