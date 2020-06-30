from math import floor

import numpy as np

arr = np.ones( (5,9))
# print(arr)

num = 1
for i in range(4, -1, -1):
    for j in range(8, -1, -1):
        arr[i][j] = floor(num)
        num += 1


# converting the data type from float to int  
newArr = arr.astype(int)


