def odd_shortcut(s: str):
    return ''.join([c for c in s if int(c) % 2 != 0])


def odd_shortcut_easier(s: str):
    return ''.join([c for c in s if c in "13579"])


def odd_shortcur_easier_2(s: str):
    result = ""
    for c in s:
        if int(c) % 2 == 1:
            result += c
    return result


def zad3_2():
    numbers_without_odd_shortcut = 0
    biggest_number_without_odd_shortcut = 0
    with open("skrot_przyklad.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip("\n\r")
            if not odd_shortcut(line):
                numbers_without_odd_shortcut += 1
                if (biggest_number_without_odd_shortcut < int(line)):
                    biggest_number_without_odd_shortcut = int(line)
    print(
        f"Liczb bez nieparzystych cyfr: {numbers_without_odd_shortcut}, a największa z nich to: {biggest_number_without_odd_shortcut}")


if (__name__ == "__main__"):
    zad3_2()
