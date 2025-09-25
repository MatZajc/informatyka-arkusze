def zad4_3():
    with open("liczby_przyklad.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        first_line_numbers = sorted(
            [int(x) for x in lines[0].strip("\n\r").split(" ")])
        second_line_numbers = sorted(
            [int(x) for x in lines[1].strip("\n\r").split(" ")])
# TODO!
