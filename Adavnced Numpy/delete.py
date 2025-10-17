"""
np.delete(arr,index,axis=none)

flattened array 
"""

import numpy as np 

arr = np.array([1,2,3,5,6,8,9])
print(arr)
new_arr=np.delete(arr,5)
print(new_arr)