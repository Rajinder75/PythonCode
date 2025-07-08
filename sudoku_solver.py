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


