def arithmetic_arranger(problems, show_answers=False):
    line_1=""
    line_2=""
    line_3=""
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        for operation in problems:
            element_list = operation.split()

            if element_list[1] != "+":
                if element_list[1] != "-":
                    return "Error: Operator must be '+' or '-'."

            elif (element_list[0].isdigit() == False) or (element_list[2].isdigit()==False):
                return 'Error: Numbers must only contain digits.'

            elif ((len(element_list[0])<=4)==False) or ((len(element_list[2])<=4)==False):
                return 'Error: Numbers cannot be more than four digits.'

            else:
                if len(element_list[0]) > (element_list[2]):
                    line_1 += element_list[0] + " "*4
                    line_2 += element_list[1] + " "*(element_list[])



                #line_1 += element_list[0] + " "*4
                #line_2 += element_list[1] + " " + element_list[2]
                #line_3 += "_"*len(line_2)
                
        #problems = line_1 + "\n" + line_2 + "\n" +  line_3
    #return problems

#print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
