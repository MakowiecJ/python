def ruler(length):
    L = []
    for i in range(length):
        L.append('|....')
    L.append('|\n')
    for i in range(length + 1):
        L.append('{}    '.format(i))
    return("".join(L))

def grid(rows, cols):
    row1 = '----'.join('+' * (cols+1)) + '\n'
    row2 = '    '.join('|' * (cols+1)) + '\n'
    L = []
    for i in range(rows):
        L.append(row1+row2)
    L.append(row1)
    return(''.join(L))

print(grid(2,3))
print(ruler(3))