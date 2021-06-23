# Python100CasesPractice
   
   100 practical cases
    
   Original git url: 
    
   https://github.com/RichardFu123/Python100Cases

## Cases I modified
- p69 
   
    Rewrite the entire problem

- p74

    Combined the two lists in one function

- p76

    Simplified the functions
    
- p78

    Used the inner function of python dict()
    
- p85

    Rewrite the entire problem by using the string's feature

- p88

    Use the random list to generate the stars

- p93 
    
    Python 3.8 has abandoned the time.clock(), used the time.perf_counter() instead

## Useful functions and notes

- Generate a random list

    import random as rd

    rd.sample([i for i in range(n)], n)
    
- Generate a matrix

    import numpy as np
    
    np.mat(np.arange(1, 10).reshape(3, 3))

- Get matrix row and colum
    
    mat[0]
    
    mat[:,0]
