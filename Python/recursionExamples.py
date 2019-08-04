def recMult(x, y):
    if y == 1:
        return x
    return recMult(x, y - 1) + x

def fact(n):
    if n < 3:
        return n
    return fact(n - 1) * n

def iterFact():
    numba = input('Whatcho favorite numba?\n')
    while numba > 2:


