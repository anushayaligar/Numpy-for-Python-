# it is the changing which changes the one data type to another 
import numpy as np 

arr = np.array([4.5,6.7,8.9])
print(arr.dtype)
int_arr=arr.astype(int)

print(int_arr)
print(int_arr.dtype)


