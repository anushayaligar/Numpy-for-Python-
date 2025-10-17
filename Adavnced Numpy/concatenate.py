"""
it will add the array together 
np.concatenate((arr1,arr2),axis=0)
axis = 0 (vertical stacking )
axis = 1(horizontal stacking )
"""
import numpy as np 
arr1=np.array([3,4,5])
arr2=np.array([1,3,8])

new_arr=np.concatenate((arr1,arr2),axis=0)

print(new_arr)