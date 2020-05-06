import sys
def pattern(s):
    j = 0
    i = j + 1
    A = [0] * len(s) 
    while( i < len(s)):
        if s[j] == s[i]:
            A[i] = j + 1
            i += 1
            j += 1

        else:
            if j == 0:
                i += 1
            else:
                j = A[j -1]

    print(s)
    print(A)




pattern(sys.argv[1])
