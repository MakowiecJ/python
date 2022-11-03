# Przykłady budowania słowników
A = {}
A['I'] = 1
A['V'] = 5

L = [('X', 10), ('L', 100)]
B = dict(L)

C = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values = [1, 5, 10, 50, 100, 500, 1000]
D = dict(zip(keys, values))

print(A)
print(B)
print(C)
print(D)

# ------------------------------------------------
def roman2int(roman):
    D = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    int = 0
    i = 0
    while i < len(roman):
        if i+1 < len(roman) and roman[i:i+2] in D:
            int += D[roman[i:i+2]]
            i += 2
        else:
            int += D[roman[i]]
            i += 1
    return int

print(roman2int("IV"))
print(roman2int("IX"))
print(roman2int("XI"))
print(roman2int("XIV"))
