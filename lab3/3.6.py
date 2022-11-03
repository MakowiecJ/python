x = int(input("Podaj dlugosc x: "))
y = int(input("Podaj wysokosc y: "))

row1 = '---'.join('+' * (x+1)) + '\n'
row2 = '   '.join('|' * (x+1)) + '\n'
L = []
for i in range(y):
    L.append(row1+row2)
L.append(row1)
print(''.join(L))