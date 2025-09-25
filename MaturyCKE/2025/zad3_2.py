def is_inside_rect(x, y, rect):
    x1, y1, x2, y2 = rect
    return x1 < x < x2 and y1 < y < y2


def zad3_2():
    positions = [(0, 0)]
    with open("dron.txt", mode='r', encoding='utf-8') as f:
        lines = [line.strip("\r\n") for line in f.readlines()]
    for i in range(0, len(lines)):
        line = lines[i].split()
        x, y = int(line[0]), int(line[1])
        curr_pos = positions[i][0] + x, positions[i][1] + y
        positions.append(curr_pos)
    number_of_pos_inside = sum([(1 if is_inside_rect(
        elem[0], elem[1], (0, 0, 5000, 5000)) else 0) for elem in positions])
    print(number_of_pos_inside)

    for left in range(len(positions)):
        for right in range(len(positions)-1, left+1, -1):
            for middle in range(left+1, right):
                if ((positions[left][0]+positions[right][0])/2 == positions[middle][0] and
                   (positions[left][1]+positions[right][1])/2 == positions[middle][1]):
                    print(positions[left], positions[middle], positions[right])
                    break


zad3_2()
