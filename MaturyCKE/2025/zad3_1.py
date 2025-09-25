def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def zad3_1():
    gcd_greater_than_one = 0
    with open("dron.txt", mode='r', encoding='utf-8') as f:
        lines = [line.strip("\r\n") for line in f.readlines()]

    for line in lines:
        line = line.split()
        a, b = int(line[0]), int(line[1])
        if abs(gcd(a, b)) > 1:
            gcd_greater_than_one += 1
    print(gcd_greater_than_one)


zad3_1()
