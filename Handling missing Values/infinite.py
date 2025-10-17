# np.isinf(arr)

import numpy as np
arr=([2,3,4,np.inf,8,9,-np.inf])
print(np.isinf(arr))#here we have found out that teh infinite number is present

# now we will do how to replace the infinite num to some finite num
cleaned_arr=np.nan_to_num(arr,posinf=1000,neginf=-1000)
print(cleaned_arr)