"""
np.insert(arr,index,value,axis)
arr = the noraml array
index = index no
value = what value u r going to add 
axis = 0 for row wise change
axis = 1 for column wise change
axis = none it will assign the values in flatten like in single line 
either if we dont mention any axis the default it will be row

"""

import numpy as np 

arr =np.array([1,2,3,4,5,6])

print(arr)
new_arr=np.insert(arr,2,9,0)
print(new_arr)