liczby = []
aktualny_podciag = 0
poprzednia_liczba = 0
max_podciag = 0

with open("dane8.txt", mode='r') as openfile:
    for line in openfile:
        liczba = int(line.strip("\n\r"))

        if(liczba > poprzednia_liczba):
            aktualny_podciag+=1
        else:
            if(aktualny_podciag > max_podciag):
                max_podciag = aktualny_podciag
            aktualny_podciag = 1

        poprzednia_liczba = liczba

    if(aktualny_podciag > max_podciag):
        max_podciag = aktualny_podciag
    
    print(max_podciag)
        
        
