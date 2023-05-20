import numpy as np

array1 = np.array([1,2,3,4,5,6,7,8,9,10], float)
print("first array:\n", array1)

array2 = array1.reshape(5,2)
print("first array, reshaped:\n", array2)

twoD_array = np.array([[1,2,3],[4,5,6]], float).reshape((2,3))
print("2D array:\n", twoD_array)

reshape_2d = twoD_array.transpose()
print("2D array, transposed:\n", reshape_2d)

array_a = np.array([[1,2],[3,4]],float)
array_b = np.array([[5,6],[7,8]],float)

concat_1 = np.concatenate((array_a,array_b),axis=0)
concat_2 = np.concatenate((array_a,array_b),axis=1)

print("Array A:\n", array_a)
print("Array B:\n", array_b)
print("Concatenated by Axis 0:\n", concat_1)
print("Concatenated by Axis 1:\n", concat_2)
