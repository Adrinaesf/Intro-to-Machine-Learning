import numpy as np
'''
Filtering: 
    process of selecting elements from an array that match a given condition. 
    So we filter out the ones that don't pass it. 
'''
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65], 
                 [39, 22, 15, 99, 18, 18, 20, 21]])

# The elements that are tennagers: 
tennagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)] 
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]

print(tennagers)
print(adults)
print(seniors)
print(evens)

# PReserving the original shape of function: 
# np.where(condition, arrayName, default_value_for_filtering)
adults = np.where(ages >= 65, ages, -1)
print(adults)