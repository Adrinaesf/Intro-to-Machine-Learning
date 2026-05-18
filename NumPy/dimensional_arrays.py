import numpy as np
'''
2. Multi-dimensional arrays
    __ 2.1 dimensions of array __
        - dimensions can be 0, 1, 2, ...
        - 0: 'A'

        - 1: ['A', 'B', 'C']

        - 2: [['A', 'B', 'C'], 
              ['A', 'B', 'C'], 
              ['A', 'B', 'C']]

        - 3: [[['A', 'B', 'C'], 
              ['A', 'B', 'C'], 
              ['A', 'B', 'C']], 

              [['A', 'B', 'C'], 
              ['A', 'B', 'C'], 
              ['A', 'B', 'C']], 
              
              [['A', 'B', 'C'], 
              ['A', 'B', 'C'], 
              ['A', 'B', 'C']]]

        - We need a consistant number of elements in arrays. 
        - Methods: 
            . np.array()
            . array.shape
            . array.ndim --> return the dimension. 

    __ 2.2 Accessing the data __
        -  array[0, 0, 0] --> 'A'
        -  array[0, 0, 3] --> error 
        -  array[layer/block, row, elem]
'''
## 2) Multi_dimensional arrays: 
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], 
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']], 
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

## Accessing the elements, let's make my name ADRINA
my_name = array[0, 0, 0] + array[0, 1, 0] + array[1, 2, 2] + array[0, 2, 2] + array[1, 1, 1] + array[0, 0, 0]
print(my_name)