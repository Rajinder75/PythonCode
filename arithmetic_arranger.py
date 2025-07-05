def arithmetic_arranger(problems, show_answers=False):
    space = " " 
    line_1=""
    line_2=""
    line_3=""
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        for operation in problems:
            element_list = operation.split()

            if element_list[1] not in ["+", "-"]:
                return "Error: Operator must be '+' or '-'."

            elif (element_list[0].isdigit() == False) or (element_list[2].isdigit()==False):
                return 'Error: Numbers must only contain digits.'

            elif ((len(element_list[0])<=4)==False) or ((len(element_list[2])<=4)==False):
                return 'Error: Numbers cannot be more than four digits.'

            else:
                greater = max(len(element_list[0]), len(element_list[2]))

                number_of_dashes = greater + 2

                line_1 += space*(number_of_dashes-len(element_list[0]))+element_list[0]+space*4
                line_2 += element_list[1] + space*(number_of_dashes-len(element_list[2])-1) + element_list[2] + space*4
                line_3 += "-"*number_of_dashes + space*4

        arranged = line_1 + "\n" + line_2 + "\n" + line_3
        
      

    return arranged


arranged = arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'])
print(arranged)

