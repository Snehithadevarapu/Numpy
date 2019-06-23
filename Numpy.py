#reshape the array
import numpy as np
arr = np.array([0,1,2,3,4,5,6,7,8,9])
arr = np.reshape(arr,(-1,5))
print("Output: ",arr)

#replace all odd numbers in anarray with -1
import numpy as np
arr = np.array([0,1,2,3,4,5,6,7,8,9])
arr[arr%2 == 1] = -1
print("Output :",arr)

#generate custom sequences
import numpy as np
arr = np.array([1,2,3])
array = np.r_[np.repeat(arr,3),np.tile(arr,3)]
print("Output : ", array)

#common items between two python numpy arrays
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
array = np.intersect1d(a,b)
print("Output : ", array)

#to get positions where elements of two arrays match
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
array = np.where(a == b)
print(array)

#2d array containing random floats b/w 5 and 10
import numpy as np
arr = np.arange(9).reshape(3,3)
rand_array = np.random.uniform(5,10,size=(5,3))
print("Output :",rand_array)

#limit the items to 6
import numpy as np
array = np.set_printoptions(threshold=6)
arr = np.arange(15)
print("output:",arr)

#print a numpy arrayby supressing sceintific notation
import numpy as np
np.set_printoptions(suppress = False)
np.random.seed(100)
rand_arr =np.random.random([3,3])/1e3
np.set_printoptions(suppress = True, precision = 6)
print(rand_arr)

#swap two coloumns in a 2d numpy array
import numpy as np
arr = np.arange(9).reshape(3,3)
print(arr[:,[1,0,2]])

#swap two rows in a 2d numpy array
import numpy as np
arr = np.arange(9).reshape(3,3)
print(arr[[1,0,2],:])
