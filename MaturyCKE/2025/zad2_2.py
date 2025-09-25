def checkNeighbours(i, j, lines):
    char = lines[i][j]
    # top
    if (lines[i-1][j] != char or lines[i-1][j-1] != char or lines[i-1][j+1] != char):
        return False
    # middle
    if (lines[i][j-1] != char or lines[i][j+1] != char):
        return False
    # bottom
    if (lines[i+1][j] != char or lines[i+1][j-1] != char or lines[i+1][j+1] != char):
        return False
    return True


def zad2_2():
    lines = []
    resultNumber = 1
    with open("symbole.txt", mode='r', encoding='utf-8') as f:
        lines = [line.strip("\r\n") for line in f.readlines()]
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[i])-1):
            if (checkNeighbours(i, j, lines)):
                print(resultNumber, i+1, j+1)
                resultNumber += 1


zad2_2()
