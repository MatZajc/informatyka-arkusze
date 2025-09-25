przedzialy= []
max_lancuch = 0

with open("dane3.txt", mode='r') as openfile:
    for line in openfile:
        a ,b = line.strip("\n\r").split(" ")
        a = int(a)
        b = int(b)
        
        przedzialy.append([a, b, 1])

    przedzialy = sorted(przedzialy, key=lambda x :x[1] - x[0] + 1)

    for i in range(len(przedzialy)):
        for j in range(i):
            if przedzialy[j][0] >= przedzialy[i][0] and przedzialy[j][1] <= przedzialy[i][1]:
                if przedzialy[i][2] <= przedzialy[j][2] + 1:
                    przedzialy[i][2] = przedzialy[j][2] + 1

    for k in range(len(przedzialy)):
        if max_lancuch < przedzialy[k][2]:
            max_lancuch = przedzialy[k][2]

    print(max_lancuch)