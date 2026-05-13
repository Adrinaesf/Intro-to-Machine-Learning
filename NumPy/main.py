import numpy as np # type: ignore
## importing it as np for sure

## 1) Making a list of numbers: 
array = np.array([1, 2, 3, 4])
print(type(array))

#________________________________________________________________________________________
print("2. dimensional arrays : ________________________________________________________________________________________")
## 2) Multi_dimensional arrays: 
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], 
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']], 
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

## Accessing the elements, let's make my name ADRINA
my_name = array[0, 0, 0] + array[0, 1, 0] + array[1, 2, 2] + array[0, 2, 2] + array[1, 1, 1] + array[0, 0, 0]
print(my_name)

#________________________________________________________________________________________
## 3. SLicing: 
print("3. SLICING : ________________________________________________________________________________________")
array_slice = np.array([[1, 2, 3, 4], 
                        [5, 6, 7, 8], 
                        [9, 10, 11, 12], 
                        [13, 14, 15, 16]])

## Let's slice it using: array_slice[start:end:step]
## The ending is exclusive and not counted
## print(array_slice[::-2])

# Col Selsection: 
print(array_slice[:, 1]) # Second col
print(array_slice[:, 0:3]) # first three col: start at col 0, to col 3
print(array_slice[:, ::-2])# Printing the col with steps starting from the end and step 2


# row and col selection: 
# First two row and two col:
print(array_slice[0:2, 0:2])
#last two row and col 1 to 3: 
print(array_slice[2: , 2: ])

#________________________________________________________________________________________
# 4. ARithmetic: 
# Adding and subtracting: 
array_arithmetic = np.array([1.1, 2.6, 4])
print("4. ARITHMETICS: ________________________________________________________________________________________")
print("Scalar: ")
print(array_arithmetic + 1)
print(array_arithmetic - 2)
print(array_arithmetic * 3)
print(array_arithmetic /4)
print("Vectorized math functions: ")
# Applying a whole function to the whole array without running loops: 
print(np.sqrt(array_arithmetic))
print(np.round(array_arithmetic))
print(np.pi)

radii = np.array([1, 2, 3])
## Fincting the areas of the cirscle with the radiuses in radii
print("Area: ")
print(np.pi * radii ** 2)

