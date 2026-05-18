import numpy as np
'''
5. Broadcasting: 
    1. Definition: 
        - Broadcasting allows numpy to perform operations on arrays
        - with different shapes by virtually expanding the dimensions of array
        - so that they math the larger array's shape
    
    2. Rules: 
        - 1. The dimensions have the same size: 
        - 2. Or one of the dimensions is 1. 

'''
print("Brodcasteables: ")
arr1 = np.array([[1, 2, 3, 4]])
arr2 = np.array([[1], [2], [3], [4]])

# The shapes: 
print(arr1.shape)
print(arr2.shape)

# Result: 
# (1, 4)
# (4, 1)

# Since each x, y corespondence have a 1, they can be brodcats: 
# (2, 4) and (4, 1) cant cause there is no one in 2, 4 (the x correspondence)
print(arr1 + arr2)

print("Another Example:")
# Example: 
arr3 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
arr4 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
 
print(arr3.shape)
print(arr4.shape)
print(arr3 * arr4)



