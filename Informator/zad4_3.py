liczby = []
with open("dane4.txt", mode='r') as openfile:
    for line in openfile:
        liczby.append(int(line.strip("\n\r")))

max_par = 0
najwieksze_i = -1
for i in range(len(liczby)):
    liczba_par = 0
    for j in range(i):
        if(liczby[i] > liczby[j]):
            liczba_par+=1
    if(max_par < liczba_par):
        max_par = liczba_par
        najwieksze_i = i
print(najwieksze_i+1)