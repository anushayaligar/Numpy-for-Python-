#  np.nan_to_num(array,nan=value) ,default = 0 
import numpy as np
arr=np.array([3,5,np.nan,9,np.nan])
new_arr =np.nan_to_num(arr,nan=67)
print(new_arr)