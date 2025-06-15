def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    """
    Finds the square root of a number using bisection technique

    Parameters:
    square_target (float): number whose square root is to be found
    tolerence (float): the room for error/difference
    max_iterations (integer): the number of times the loop will run to find the converging point

    Makes use of functions: none

    Returns: square root of the number
    """

    #because the sqaure root of a negative number is not real (it is imaginary)
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    

    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')

    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:

        low = 0

        #the max funcnction returns the max value from the values provided
        high = max(1, square_target)

        #defining root varibale to store the root, if found
        root = None
        
        for _ in range(max_iterations):

            #calculates the midpoint and squares it 
            mid = (low + high) / 2
            square_mid = mid**2

            # check if the difference of the square of the mid point is equal to square target (some error is ignored (tolerance))
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break
            
            # if the sqaure mid is less than the square target then the low is made equal to mid (values less than that are not considered)
            elif square_mid < square_target:
                low = mid

            # if the square mide is more than the square target, the high is made the mid (values greater than the mid are discarded)
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

N = 16
square_root_bisection(N)
