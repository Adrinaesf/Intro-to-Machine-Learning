import numpy as np
'''
aggregate functions: 
- Summerize data an dtypically return a single value. 
- Exmple: 
    . np.sum(arr)
    . np.mean(arr)
    . np.std(arr)
    . np.var(arr)
    . np.min(arr)
    . np.max(arr)

    . position of max/min value (return the index)
    . np.argmin(arr)
    . np.argmax(arr)

    . suming through col/row: 
    . np.sum(arr, axis=0) (col)
    . np.sum(arr, axis=1) (row)
    

'''
array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.argmin(array))
print(np.argmax(array))

print("Sum through the columns:")
print(np.sum(array, axis=0))

print("Sum through the rows:")
print(np.sum(array, axis=1))


