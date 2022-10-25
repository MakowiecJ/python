L = [123, 515, 12, 1, 5, 73, 346]

def toString(L):
    s = []
    for i in L:
        s.append(str(i).zfill(3))
        s.append(" ")
    return "".join(s)

print(toString(L))