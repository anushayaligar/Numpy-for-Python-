"""
to combine the multiple arrays 

Vstack = rowwise
hstack = columnwise 

"""
import numpy as np

arr1 = np.array([10,20,30,40,50])
arr2 = np.array([60,70,80,90,100])

print(np.vstack((arr1, arr2)))

print(np.hstack((arr1, arr2)))
