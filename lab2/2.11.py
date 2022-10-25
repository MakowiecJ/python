# "abc" -> "a_b_c"

def foo(word):
    newWord = []
    for c in word[:-1]:
        newWord.append(c + "_")
    newWord.append(word[-1])
    return "".join(newWord)

print(foo("abc"))
print(foo("a"))