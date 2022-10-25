line = "abcdefghijklmnouprstwxyz"

w1 = []
w2 = []

for c in line[:3]:
    w1.append(c)

for c in line[-3:]:
    w2.append(c)

print("".join(w1))
print("".join(w2))