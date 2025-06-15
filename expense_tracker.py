def add_expense(expenses, amount, category):
    """
    Appends amount and the category of the expense into a list in the form of dictionary

    Parameters:
    expenses (list): The list in which the expense is stored
    amount (float) : The expense amount
    category (string) : Category of the expense

    Makes use of functions: none

    Returns: none
    """
    expenses.append({'amount': amount, 'category': category})

    
def print_expenses(expenses):
    """
    Prints the expenses and the category by iterating through the list

    Parameters:
    expenses (list): The list in which the expense is stored

    Makes use of functions: none

    Returns: none
    """
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    """
    Calculates the sum of expenses

    Parameters:
    expenses (list): The list in which the expense is stored

    Makes use of functions: none

    Returns: The sum of expenses
    """
    #map applies a given function (lambda here) to a given iterable (expenses here.)
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    """
    Filters the expenses  based on the desired category and returns them.

    Parameters:
    expenses (list): The list in which the expense is stored
    category (string) : Category of the expense

    Makes use of functions: none

    Returns: expenses after filtering based upon the passed category 
    """

    #the filter function filters an iterable (expensez) based on a given condition. It takes two arguments a function (lambda) and an iterable
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    """
    Asks the user about the task and calls the appropriate fucntions accordingly.

    Parameters: none

    Makes use of functions: add_expense, print_expenses, total_expenses, filter_expenses_by_category

    Returns: none
    """
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            # filtered expenses are stored in the expenses_from_category variable
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

main()