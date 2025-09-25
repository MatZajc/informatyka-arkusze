p_minimalne_suma_max = [0 for _ in range(9)]
p_minimalne_max = ["" for _ in range(9)]

with open("dane6.txt", mode='r') as openfile:
    for line in openfile:
        liczba = line.strip("\n\r")

        max_znak = 1
        for znak in liczba:
            if(int(znak) > max_znak):
                max_znak = int(znak)
        suma_cyfr = sum([int(x) for x in liczba]) 
        if(suma_cyfr > p_minimalne_suma_max[max_znak-1]):
            p_minimalne_suma_max[max_znak-1] = suma_cyfr
            p_minimalne_max[max_znak-1] = liczba

for i in range(0, len(p_minimalne_max)):
    print(i+2, p_minimalne_max[i])


        