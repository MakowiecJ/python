L = [[],[4],(1,2),[3,4],(5,6,7)]
L2 = []

for i in L:
    sum = 0
    for j in i:
        sum += j
    L2.append(sum);

print(L2)