import sys


def egg_drop_prob(n, e):
    # assigning data sturucture 
    edp = [[0 for __ in range(e + 1)] for __ in range(n + 1)]

    # setting base case
    for i in range(n+1):
        edp[i][1] = i  # when you have one egg; no of drops = no of foors we have.
    for i in range(e+1):
        edp[1][i] = 1  # when we have 1 floor ; no of drops = 1

    # executing formulae
    for i in range(2,n+1):
        for j in range(2,e+1):
            edp[i][j] = sys.maxsize
            for x in range(1,n):
                temp = max(edp[i-x][j], edp[x-1][e-1])+1
                if temp < edp[i][j]:
                    edp[i][j] = temp

    return edp[n][e]


print("Minimum attempts")
print(egg_drop_prob(100, 2))


