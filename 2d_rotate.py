# rotate 2D matrix - SQUARE

def sp(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j],end=" ")
        print("\n")
        

arr = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
        ]

sp(arr)

arr2 = [[0 for __ in range(len(arr))] for __ in range(len(arr))]

for r in range(len(arr)):
    for c in range(len(arr)):
        #arr2[len(arr)-1-c][r] = arr[r][c] # anti clock
        arr2[c][len(arr)-1-r] = arr[r][c] # clock

sp(arr2)


