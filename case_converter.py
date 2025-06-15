def convert_to_snake_case(pascal_or_camel_cased_string):
    """
    Changes strings from CamelCase/PascalCase to snake_case

    Parameters:
    pascal_or_camel_cased_string(string): a string which is in Pascal or Camel case  

    Makes use of functions: none

    Returns: a string in snake case
    """
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))
main()