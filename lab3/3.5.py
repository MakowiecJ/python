length = int(input("Podaj dlugosc miarki: "))

L = []
for i in range(length):
    L.append('|....')
L.append('|\n')
for i in range(length + 1):
    L.append('{}    '.format(i))
print("".join(L))