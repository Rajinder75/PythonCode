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

Movements (in any direction) are allowed between rods under the below conditions:
(I) The allowed disk movements between the rods exhibit a repetitive pattern occurring every three
moves. For example, movements between rod A and rod C are allowed on the first, the fourth and the
seventh move, where the remainder of the division between the move number and 3 is equal to 1.

(II) When the remainder of the move number divided by 3 is equal to 2, the movement is allowed between
'A' and 'B' (the source and the auxiliary rods).

(III) When the move number divided by 3 has no remainder, the movement is allowed between
 'B' and 'C'.
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

#rod 2 here is the target rod
def make_allowed_move(rod1, rod2):
    #The below variable will be used to check the direction of movement
    forward = False #prevents the movement from source to target

    #When target is empty, the disk should be moved necessarily from source to target.
    if not rods[rod2]:
        forward = True #allows movement from source to target because target is empty
    #The other case in which you have to move the disk necessarily from source to target 
    #is when the source list is not empty and the last disk in source is lower 
    #than the last disk in target.
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True

    #the below excecutes when the forward is set to True
    if forward:
        #print the move
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        #removing the disc from source (pop) and adding it to target (append)
        rods[rod2].append(rods[rod1].pop())
                
    #if the forward is set to false (movement from target to source, backward direction)
    else:
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())
    print('display our progress')
    print(rods,"\n")

#the below approach uses iterative approach
#source rod is A, auxiliary rod is B and target rod is C (function parameters)
def move(n, source, auxiliary, target):
    #display starting configuration
    print(rods,"\n")
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:

            #executes when n is odd
            if n%2 != 0:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            #executes when n is even
            else:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                #calling make_allowed_move() to make the move
                make_allowed_move(source, auxiliary)  

        elif remainder == 2:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            #calling make_allowed_move() to make the move
            make_allowed_move(auxiliary, target)

#initiate call from source A to target C with auxiliary B.
move(NUMBER_OF_DISKS, 'A', 'B', 'C')