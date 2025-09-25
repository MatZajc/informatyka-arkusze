A = [2,4,6,8,10,9,7,5,3,1]

def procedura(j):
    if(j > 0):
        if(A[j] < A[j-1]):
            v = A[j]
            A[j] = A[j-1]
            A[j-1] = v
            procedura(j-1)

def procedura_iter(j):
    while(j > 0):
        if(A[j] < A[j-1]):
            v = A[j]
            A[j] = A[j-1]
            A[j-1] = v
        else:
            break
        j-=1

def proc(i):
    while(i>0):
        if(A[i] < A[i-1]):
            help = A[i]
            A[i] = A[i-1]
            A[i-1] = help
        else:
            break
        i -= 1

B = A.copy()

procedura(7)
print(A)

A = B

proc(7)
print(A)
