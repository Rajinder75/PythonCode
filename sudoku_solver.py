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

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            #row will store the row number and the contents will store the list representing the row

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
        return all((self.board[row][col] != num for row in range(9)))

    #To check if the number can be entered in a 3by3 square
    def valid_in_square(self, row, col, num):
        #calculates the starting row index of a 3×3 box in a Sudoku puzzle.
        row_start = (row//3)*3
        #similarly for columns
        col_start = (col // 3) * 3

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
        return all([valid_in_row, valid_in_col, valid_in_square])

    #This method will solve the puzzle in place rather than creating a new one
    def solver(self):

        # The := (walrus) operator gives you the ability to assign variables in the middle of an expression.
        if (next_empty:=self.find_empty_cell()) is None:
            return True
        
        #This loop will be used to check what number can be filled in a specific place in the board
        for guess in range(1,10):
            pass


    


    

#creating a object instance of a class
#This calls the constructor of the Board class, which by default is __init__()
#if you don't define one yourself. It creates a new object of that class.
gameboard = Board(puzzle)

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




# To check if a value is valid can be added to a col
# print(gameboard.valid_in_col(0, 1))

#To check if a value can be added in a 3by3 square
#print(gameboard.valid_in_square(1,0,3))