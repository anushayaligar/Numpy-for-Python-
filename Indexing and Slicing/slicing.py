# extracting the subset of data
"""
array[start:stop:step]
arr[start:end], start to end-1
negative step , -1 reverse


"""

import numpy as np 
arr = np.array([10,20,30,40,50,60])

print(arr[1:5]) # 20 to 40 prints
print(arr[:6])  #index 0 to 5 
print(arr[::2]) # prints step size of 2 
print(arr[::-1]) #reverse slicing prints reverse array
