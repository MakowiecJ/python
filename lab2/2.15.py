def toString(L):
    s = []
    for i in L:
        s.append(str(i))
    return "".join(s)

L = [1,2,3,4,5,6]

result = toString(L)

print(result)
print(type(result))
