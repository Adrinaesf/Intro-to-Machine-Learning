import numpy as np
'''
Steps: 
1. first we call the class: 
    - If we don't want to save the results: (no seed)
    rng = np.random.default_rng()
    
    random integers, with a range from low to high, and a size of numbers to generate:
    rng.integers(low=a, high=b, size(row_num, col_num)
        example: 
        rng.integers(low=1, high=4, size(3)
        = [2, 2, 3] (random)
    
    - now fixing the random numbers: 
    rng = np.random.default_rng(seed=1)

2. Floating point numbers: 
    . a floating point number has decimals: 
    . np.random.uniform(low=a, high=b, size=...)

3. Shuffele an array: 
    . we need rng 
    . so we make it: 
    . rng = np.random.default_rng()
    . array = np.array[1, 2, 3, 4, 5]
    . now we suffle: rng.shuffle(array)

4. Choosing a random element in an array: 
    . make the array
    . make rng
    . num = rng.choice(arrayName, size)
    . it will randomly choose an element in that array


'''
rng = np.random.default_rng()
print(rng.integers(low=1, high=101, size=(3,2)))

## -------------------
print("floating num:")
print(np.random.uniform(low=1, high=2, size=(3,2)))

## -------------------
print("Shuffeling an array:")
array = np.array([1, 2, 3, 4, 5])

print("array before shuffle:")
print (array)
rng.shuffle(array)
print("after shuffle:")
print(array)
## -------------------
print("Chooing a random element from array:")
fruits = np.array(["🍎", "🥑", "🍋", "🍒", "🍌"])
fruit = rng.choice(fruits, (3, 3))

print(fruit)



