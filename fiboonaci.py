def fibonnaci(idx):
    seq = [0,1]
    for i in range(idx):
        seq.append(seq[-1]+seq[-2])
    return seq[-2]



def febonacci(idx):
    if idx <= 1:
        return idx
    else:
        return febonacci(idx-1)+ febonacci(idx-2)



print(febonacci(8))
print(fibonnaci(8))