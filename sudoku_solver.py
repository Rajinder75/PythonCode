#class definition
class Board:
    #instance method always start with self as a first parameter.
    #When you define a method inside a class and call it using an object, Python automatically passes
    #the object as the first argument. self receives that object.
    def __init__(self, board):
        #If you define a method called __init__ inside your class,
        #you can set up the object with custom data right when it’s created.

        # stores the value you pass during creation into the object itself.
        self.board = board

    
    # The __str__ method is a special method that is called under the hood when the object is
    #  printed using the print() function, or converted into a string using the str() function
    #give a string only when the item is not zero, and an asterisk character otherwise.
        def __str__(self):
            board_str = ''
            #using a for loop to iterate over each row in the board
            for row in self.board:
                #The belwo is called list comprehension with an if and else
                row_str = [str(i) if i else '*' for i in row]
                board_str += ' '.join(row_str)
                board_str+= "\n"
            return board_str
            


    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            #enumerate - row will store the row number and the contents will store the list representing the row

            try:
                #Locating the  empty cell which is filled with number 0
                col = contents.index(0) #.index() raises ValueError if 0 is not found

                #returns row index and column index
                return row, col
            except ValueError:
                pass

        #This handles the case when no cell is found empty (indicating the board is full)
        return None
    
    # checks if a given number can be inserted into a specified row of the sudoku board.
    #RULE - A number can be inserted into a row if it is not already present in that row.
    def valid_in_row(self, row, num):
        #checking if the number is not in the row
        #returns True if not present in row and False otherwise
        return num not in self.board[row]
    
    #Similar to above function but for columns
    def valid_in_col(self, col, num):
        #checks if the number in that column for all rows
        #column number stays same but row number changes (because of range and for loop)
        #this is an example of generator expression

        # all() function checks if all the elements in the column are different from num
        #range is used to iterate over all rows, while column remains constant
        return all((self.board[row][col] != num for row in range(9)))


    #To check if the number can be entered in a 3by3 square
    def valid_in_square(self, row, col, num):
        #calculates the starting row index of a 3×3 box in a Sudoku puzzle.
        row_start = (row//3)*3
        #similarly for columns
        col_start = (col // 3) * 3

        """
            Suppose you want to check the cell at row 5, column 7.
            row_start = (5 // 3) * 3
            5 // 3 is 1, so 1 * 3 = 3
            So, row_start = 3

            col_start = (7 // 3) * 3
            7 // 3 is 2, so 2 * 3 = 6
            So, col_start = 6

            This means the 3x3 square starts at row 3, column 6.
            The square covers rows 3–5 and columns 6–8
        """

        #to iterate over 3 rows of a valid 3by3 sqaure
        for row_no in range(row_start, row_start+3):
            for col_no in range(col_start, col_start + 3):
                #checking if the given number is present in 3by3 square
                if self.board[row_no][col_no] == num:
                    #returning false if it is present, then the number will not be inserted
                    return False
                
        #executes only if the number is not present in the 3by3 square,
        #which means that the number can be inserted
        return True
    
    #This method will check if a given number is a valid choice for an empty cell in the sudoku board by
    #validating its compatibility with the row, column, and 3x3 square of the specified empty cell

    #empty is a tuple representing the row and column indices of empty cell
    def is_valid(self, empty, num):
        #unpacking the tuple
        row, col = empty

        #checking if the number is valid for insertion in the specified row.
        #self is used to reference the methods of current instance
        valid_in_row = self.valid_in_row(row, num)

        #checking its validity for insertion in column
        valid_in_col = self.valid_in_col(col, num)
        #checkign its validity for insertino in 3by3 sqaure
        valid_in_square = self.valid_in_square(row, col, num)

        #To verify the number in all those checks
        #Because of all(), it returns True only if all checks are True
        return all([valid_in_row, valid_in_col, valid_in_square])

    #This method will solve the puzzle in place rather than creating a new one
    def solver(self):

        # The := (walrus) operator gives you the ability to assign variables in the middle of an expression.
        #Observe that the assignment and the conditional statement are combines in a single line
        if (next_empty:=self.find_empty_cell()) is None: #This is true when the sudoku is full
            return True
        
        #This loop will be used to check what number can be filled in a specific place in the board
        #the range covers 1 to 9 inclusive
        for guess in range(1,10):
            #next_empty is the tuple with the row and column indices of the empty cell,
            #and guess is the number (1 to 9)
            if self.is_valid(next_empty, guess): #This is true only if the guess is valid to be inserted at the place which is empty
                row, col = next_empty
                self.board[row][col] = guess
                
                #Recursive call to the solver method
                if self.solver():  #This will stop the recursive calls when the sudoku is solved
                    return True
                # If the recursive call returns False, it means the guess led to an unsolvable 
                # sudoku. So you'll need to restore the cell to be empty and explore another guess.
                self.board[row][col] = 0
        # the solver method return False if none of the guesses leads to a solution
        return False
    


def solve_sudoku(board):
    #assigning the instance of the Board class to gameboard
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')

    if gameboard.solver() == True:
        print(f'Solved puzzle:\n{gameboard}')
    #when the puzzle is not solvable
    else:
        print('The provided puzzle is unsolvable.')

    #returning the final instance of the board class
    return gameboard

#creating a object instance of a class
#This calls the constructor of the Board class, which by default is __init__()
#if you don't define one yourself. It creates a new object of that class.

"""
You can call a instance method using dot notation:

instance_name.method_name()
here instance_name is the instance or object

"""



puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)


# To check if a value is valid can be added to a col
# print(gameboard.valid_in_col(0, 1))

#To check if a value can be added in a 3by3 square
#print(gameboard.valid_in_square(1,0,3))