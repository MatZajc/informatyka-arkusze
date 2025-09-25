liczby = []

max_dlugosci = []

with open("dane8.txt", mode='r') as openfile:
    for line in openfile:
        liczba = int(line.strip("\n\r"))

        liczby.append(liczba)

    for i in range(len(liczby)):
        max_dlugosci.append(1)
        for j in range(i):
            if(liczby[j] < liczby[i]):
                if(max_dlugosci[j]+1 > max_dlugosci[i]):
                    max_dlugosci[i] = max_dlugosci[j]+1

print(max(max_dlugosci))

            

    
        
        
