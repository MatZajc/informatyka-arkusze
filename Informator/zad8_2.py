liczby = []

ile_par = 0

with open("dane8.txt", mode='r') as openfile:
    for line in openfile:
        liczba = int(line.strip("\n\r"))

        liczby.append(liczba)

for i in range(len(liczby)):
    for j in range(i, len(liczby)):
        if(liczby[i] > liczby[j]):
            ile_par+=1

print(ile_par)
