p_minimalne = [0 for _ in range(9)]

with open("dane6.txt", mode='r') as openfile:
    for line in openfile:
        liczba = line.strip("\n\r")

        max_znak = 1
        for znak in liczba:
            if(int(znak) > max_znak):
                max_znak = int(znak)
        p_minimalne[max_znak-1] += 1
for i in range(0, len(p_minimalne)):
    print(i+2, p_minimalne[i])
                