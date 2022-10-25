def countWords(line):
    i = 0
    for word in line.split():
        i += 1
    return i

line = "ada deanm  mnamsd dasdmn"
print(countWords(line))