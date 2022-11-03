L1 = [1,2,3,4]
L2 = [3,4,5,6]

# a)
L = list(set(L1) & set(L2))
print(L)

# b)
L = list(set(L1) | set(L2))
print(L)