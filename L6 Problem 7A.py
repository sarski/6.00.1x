def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L
    
def addOne(n):
    return n + 1

def square(n):
    return n ** 2