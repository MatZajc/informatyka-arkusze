wystepowanie = {chr(litera) : 0 for litera in range(65,91)}
dekoder = {chr(litera) : "0" for litera in range(65,91)}

with open("szyfrogram.txt", mode='r') as openfile:
    for line in openfile:
        slowo = line.strip("\n\r")

        for znak in slowo:
            wystepowanie[znak] += 1

with open("czestosc.txt", mode='r') as openfile:
    for line in openfile:
        key, value = line.strip("\r\n").split(" ")
        value = int(value)

        for klucz in wystepowanie:
            if(wystepowanie[klucz] == value):
                dekoder[klucz] = key
                break
    print(dekoder)

for litera in "CAIMURJH":
    print(dekoder[litera], end="")
print()


with open("szyfrogram.txt", mode='r') as openfile:
    for line in openfile:
        slowo = line.strip("\n\r")

        for znak in slowo:
            print(dekoder[znak], end="")
        print()






