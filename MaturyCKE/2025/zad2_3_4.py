charMap = {
    "o": 0,
    "+": 1,
    "*": 2
}


def translateFromBaseThreeChar(s):
    """
    Translate a string of characters to a base-3 number.
    """
    result = 0
    for c in s:
        result = result * 3 + charMap[c]
    return result


def zad2_3():
    currentMax = 0
    currentMaxCharRepr = ""
    with open("symbole.txt", mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip("\r\n")
            converted = translateFromBaseThreeChar(line)
            if converted > currentMax:
                currentMax = converted
                currentMaxCharRepr = line
    print(currentMax, currentMaxCharRepr)


zad2_3()


def translatetoToBaseThreeChar(num):
    result = ""
    while (num > 0):
        r = num % 3
        num = num // 3
        if (r == 0):
            result += "o"
        elif (r == 1):
            result += "+"
        else:
            result += "*"
    return result[::-1]  # reverse the string to get the correct order


def zad2_4():
    result = 0
    with open("symbole.txt", mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip("\r\n")
            result += translateFromBaseThreeChar(line)
    print(result, translatetoToBaseThreeChar(result))


zad2_4()
