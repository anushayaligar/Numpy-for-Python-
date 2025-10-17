import numpy as np 

arr = np.array([[1,3],[4,5]])
print(arr)
new_arr=np.insert(arr,2,[8,5],0)
print(new_arr)