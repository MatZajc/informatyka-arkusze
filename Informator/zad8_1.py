poprzednia_liczba = -1
parzyste_luki = 0
nieparzyste_luki = 0

with open("dane8.txt", mode='r') as openfile:
    for line in openfile:
        liczba = int(line.strip("\n\r"))

        if(poprzednia_liczba == -1):
            poprzednia_liczba = liczba
            continue

        roznica = abs(poprzednia_liczba - liczba)
        if(roznica % 2 == 1):
            nieparzyste_luki+=1
        else:
            parzyste_luki+=1
        poprzednia_liczba = liczba
print(parzyste_luki, nieparzyste_luki)
