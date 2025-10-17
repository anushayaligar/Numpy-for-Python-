"""

#  this both basically use to convert the multi deminsional array into 1D
.ravel -> view (means it will change the original array)
.flatten()-> copy (it will keep the original array as it is )


"""

import numpy as np 

arr = np.array([[1,2,3],[4,5,6]])
print(arr.ravel())
print(arr.flatten())