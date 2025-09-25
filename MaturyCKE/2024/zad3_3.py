from zad3_2 import odd_shortcut


def gcd2(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a


def zad3_3():
    with open("skrot2_przyklad.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip("\n\r")
            odd_shorted = odd_shortcut(line)

            if gcd(int(line), int(odd_shorted)) == 7:
                print(line)


if (__name__ == "__main__"):
    zad3_3()
