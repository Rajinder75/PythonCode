"""
The algorithm works like this:
1. divides an unsorted sequence into subparts
2. sort items in subparts
3. merge the sorted subparts


-- a list with a single element is always sorted
"""

def merge_sort(array):

    #In recursive solutions, a base case is required to stop the execution of the function
    if len(array) <= 1:
        return

    middle_point = len(array)//2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    #calling merge_sort recursively to sort the sub lists
    merge_sort(left_part)
    merge_sort(right_part)

    #variables to hold index values that will be used for comparison
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    #checks if the the indices are less than the length of the lists
    while left_array_index < len(left_part) and right_array_index < len(right_part):

        #checks if the element of left part is less than the corresponding element in right part
        if left_part[left_array_index] < right_part[right_array_index]:

            #assigns the smallers elemetn to the array at the sorted index (0th index, then 1st index and so on)
            array[sorted_index] = left_part[left_array_index]

            #PAY ATTENTION: As the first element of left_part is found to be smaller, the second element
            #of left_part has to then be compared to the first element of right_part
            left_array_index +=1

        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index +=1

        # to add the next sorted element on the next index
        sorted_index +=1

    #When the loop stops, there could be some elements still left in either left_part or right_part    
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index +=1
        sorted_index +=1

    #for right_part
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

#This checks if the python script is the main program or an imported module.
#If this is not written, whenever the file is imported as a module, all the functions will be executed
if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)

    print("Sorted array: "+str(numbers))
    

    
        

    

