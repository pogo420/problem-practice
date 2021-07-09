arr = [[0,1,1,1],
        [1,0,1,1],
        [1,1,1,1]]

m = len(arr)
n = len(arr[0])

is_col = False
for i in range(m):
    for j in range(n):
        print(arr[i][j], end=" ")
    print("\n", end="")
print("------"*5)

for i in range(m):
    if arr[i][0] == 0:
        is_col = True
    for j in range(1,n):
        if arr[i][j] == 0:
            arr[i][0]=0
            arr[0][j]=0

for i in range(1,m):
    for j in range(1,n):
        if not arr[i][0] or not arr[0][j]:
            arr[i][j] = 0

if arr[0][0] == 0:
    for i in range(n):
        arr[0][i] = 0
if is_col:
    for i in range(m):
        arr[i][0] = 0


for i in range(m):
    for j in range(n):
        print(arr[i][j], end=" ")
    print("\n", end="")
