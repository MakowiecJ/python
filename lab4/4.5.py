def odwracanieIter(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanieRek(L, left, right):
    if left > right: return
    else:
        L[left], L[right] = L[right], L[left]
        odwracanieRek(L, left + 1, right -1)

L1 = [0,1,2,3,4,5]
L2 = [0,1,2,3,4,5]

odwracanieIter(L1, 1, 4)
odwracanieRek(L2, 1, 4)

print(L1)
print(L2)


