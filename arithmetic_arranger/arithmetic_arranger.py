def arithmetic_arranger(problems, solve=False):
    first_row = ""
    operation_row = ""
    dash_row = ""
    answers = ""
    arranged = ""
    for problem in problems:
        splitted = problem.split()
        find_max = max(int(splitted[0]), int(splitted[2]))
        width = 2 + len(str(find_max))
        first_row += f"{splitted[0].rjust(width)}    "
        operation_row += f"{splitted[1]} {splitted[2].rjust(len(str(find_max)))}    "
        dash_row += "-" * width + "    "
        if solve == True:
            answer = eval(f"{splitted[0]} {splitted[1]} {splitted[2]}")
            justificated_answer = str(answer).rjust(width)
            answers += justificated_answer + "    "
    if solve:
        arranged = '\n'.join((first_row, operation_row, dash_row, answers))
    else:
        arranged = '\n'.join((first_row, operation_row, dash_row))
    return arranged
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))
