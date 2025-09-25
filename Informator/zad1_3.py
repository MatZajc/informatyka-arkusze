def zad1_3():

    with open("dane1_3.txt", "r") as f:
        # albo tak
        liczby = [int(x.strip('\r\n')) for x in f.readlines()]

        # albo tak
        liczby = []
        for line in f.readlines():
            line = line.strip('\r\n')
            line = int(line)
            liczby.append(line)

    maximum = -100
    for i in range(0,len(liczby)):
        suma = liczby[i]
        for j in range(i+1, len(liczby)):
            suma += liczby[j]
            if(suma > maximum):
                maximum = suma
    print(maximum)    

zad1_3()