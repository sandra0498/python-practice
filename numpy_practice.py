import numpy as np

arr = np.zeros( (5,9))
# print(arr)

num = 1
for i in range(4, -1, -1):
    for j in range(8, -1, -1):
        arr[i][j] = num
        num += 1


print(arr)
