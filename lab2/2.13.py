def sum(line):
    sum = 0
    for w in line.split():
        sum += len(w)
    return sum

line = "asdasd dsdaka mkajk a"
print(sum(line))