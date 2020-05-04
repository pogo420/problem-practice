def seq_count(inp):
    inp = int(inp)
    zero_check = 0
    seq = 0
    while True:
        if zero_check >=2:
            break
        elif inp & 1 == 0:
            zero_check += 1
        inp = inp >> 1 # movement of 1 bit to right
        seq += 1

    return seq-1


print(seq_count(1775))
        
    





