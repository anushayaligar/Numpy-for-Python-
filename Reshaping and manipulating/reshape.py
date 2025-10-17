"""
reshape(rows,colums) specify new shape 
if dimensions match
"""
import numpy as np
arr = np.array([1,2,3,4,5,6,4,5,6])
reshaped = arr.reshape(1,3)
print(reshaped)

