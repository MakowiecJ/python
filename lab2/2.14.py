#a)
def findLongest(line):
    sum = 0
    longestWord = ""
    for w in line.split():
        sum2 = len(w)
        if sum2 > sum:
            longestWord = w
            sum = sum2
    return longestWord

#b)
def longestLenght(line):
    return len(findLongest(line))

line = "ala ma kota"
print(findLongest(line))
print(longestLenght(line))