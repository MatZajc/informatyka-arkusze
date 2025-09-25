chars = ['+', 'o', '*']


def is_palindrome(s):
    """
    Check if a string is a palindrome.
    """
    return s == s[::-1]


def is_palindrome_2(s):
    for c in range(len(s) // 2):
        if s[c] != s[-c - 1]:
            return False
    return True


def zad2_1():
    with open("symbole.txt", mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip("\r\n")
            if is_palindrome(line):
                print("")
                print(line)


zad2_1()
