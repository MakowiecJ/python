def sum_seq(sequence):
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        else:
           sum += item
    return sum

L = [1, 1, 1, [1,1,1]]

print(sum_seq(L))        

