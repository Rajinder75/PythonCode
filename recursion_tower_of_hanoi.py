"""
The puzzle has 3 rods, with disks of different diameters. Initially all the disks are on the first 
rod. The biggest one is at the bottom and the smallest is at the top. 
The goal is to move the disks to the third rod by making sure no large disk is on top of a smaller one.

RULES:
1. You can move only top-most disks
2. You can move only one disk at a time
3. You cannot place larger disks on top of smaller ones

The Tower of Hanoi puzzle can be solved in 2^n-1 moves, where n is the number of disks. 

In the Tower of Hanoi puzzle, you can identify the three rods according to their purpose:

1. The first rod is the source, where all the disks are stacked on top of each other at the beginning of the game.
2. The second rod is an auxiliary rod, and it helps in moving the disks to the target rod.
3. The third rod is the target, where all the disks should be placed in order at the end of the game.
"""

#variable to store the number of disks
NUMBER_OF_DISKS = 3
#The Tower of Hanoi puzzle can be solved in 2^n-1 moves, where n is the number of disks. 
number_of_moves = (2**NUMBER_OF_DISKS)-1

# a dictionary is created having rods as keys of the dictionary
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)), #3,2,1 (if NUMBER_OF_DISKS = 3) represent rods, these are stored as a list
    'B': [],
    'C': []
}

#source rod is A, auxiliary rod is B and target rod is C (function parameters)
def move(n, source, auxiliary, target):
    #display starting configuration
    print(rods)


#initiate call from source A to target C with auxiliary B.
move(NUMBER_OF_DISKS, 'A', 'B', 'C')