def jestAntypalindromem(napis: str) -> str:
    for i in range(len(napis)//2):
        if(napis[i] == napis[-i-1]):
            return False
    return True
counter = 0
with open("dane6.txt", mode='r') as openfile:
    for line in openfile:
        liczba = line.strip("\n\r")

        if(jestAntypalindromem(liczba)):
            print(liczba)
            counter += 1
print(counter)


# counter = 0
# antypalindrom = ""

# with open("dane6.txt", mode='r') as openfile:
#     for line in openfile:
#         s = line.strip("\n\r")

#     print("-----")
#     for i in range(len(s) // 2):
#         if s[i] == s[len(s) - i - 1]:
#             counter += 1
#             antypalindrom = s
#             print(i)



#     print(antypalindrom, counter)



