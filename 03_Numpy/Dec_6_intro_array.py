# NUmpy is a library for the python programming lanugage, adding support for large files, multi-dimentional array and matrix along with a large collection of hingh level mathematics function to operate on these array.

# lists is the collection of values that holdes different types. We can perform crud operation. we generally use for data science.
# Numpy is a library for the python programming lanugage
# Calculation over entire array. easy and Fast. Installation require. Take less storeage

import numpy as np

# to 0-dimentional array
# arr1=np.array(24)
# print(arr1)
# print(arr1.ndim)

# to 1-dimentional array
l=[1,2,3,4,5,6]
arr_l = np.array(l)
print(f"Original array : {arr_l}")
# print(type(arr_l))

# opr_l = 5*l
# print(opr_l)
# op_arr_l = 5*arr_l
# print(op_arr_l)

# to check the dimention of array
# print(f"Dimention: {arr_l.ndim}")

# to check the number of rows and columns
# print(f"Number of Rows and columns: {arr_l.shape}")

# to check the size of the array
# print(f"Return no of elements : {arr_l.size}")

#  to reshape the our array
# print(f"Reshape the array in terms row and columns {arr_l.reshape(2,3)}")

# for accessing the elements of the array
# print(arr_l[3])

# zeros and ones
# print(f"zeros: {np.zeros(2)}")
# print(f"zeros: {np.ones(2)}")
# print(f"zeros: {np.zeros(2,dtype=np.int32)}")
# print(f"zeros: {np.ones(2,dtype=np.int32)}")
# print(f"zeros: {np.zeros(2,dtype=np.int32)}")
# print(f"zeros: {np.ones(2,dtype=np.int64)}")

#  2-dim array
arr2 =np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2)
# print(arr2.ndim)
# print(arr2.shape)
# print(arr2.size)
# print(arr2.reshape(3,3))
# print(arr2[0][2])
# print(arr2[0,2])

# 3-dim array
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
    ])
# print(arr3)
# print(arr3.ndim)
# print(arr3.shape)
# print(arr3.size)
# print(arr3.reshape(3,4))
