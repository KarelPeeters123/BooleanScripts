truth_table = [[False, False, False],[False, False, True],[False, True, False],[False, True, True],[True, False, False],[True, False, True],[True, True, False],[True, True, True]]
# def my_function(x, y, z):
#     return (x or y) and ((x and y) or ((not x) and z) or (not y))
# predicate = my_function
question = lambda x,y,z: not((z or (y and (not x))) and ((x and z) or (y)))

answers = [
    lambda a,b,c: ((not a) and b and c) or (b and ((a or c) and (not(a and c)))),
    lambda a,b,c: ((not a) and b and c) or (a and (not b) and c) or ((not a) and (not b) and (not c)),
    lambda a,b,c: (a and (not b) and c) or (b and ((a or c) and (not(a and c)))),
    lambda a,b,c: (a and b and c) or (a and (not b) and c) or ((not a) and (not b) and (not c))
]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

def check_all_values(fn):
    values = []
    for i in range(len(truth_table)):
        values.append(fn(truth_table[i][0], truth_table[i][1], truth_table[i][2]))
    return values
def convert_list(bool_list):
    int_list = []
    for i in range(len(bool_list)):
        int_list.append(int(bool_list[i]))
    return int_list
def print_table(results):
    # print(results)
    for i in range(len(truth_table)):
        print(convert_list(truth_table[i]), " => ", int(results[i]))
def check_answers():
    question_values = check_all_values(question)
    print_table(question_values)
    for i in range(len(answers)):
        print(letters[i], "checked!")
        answer_values = check_all_values(answers[i])
        print_table(answer_values)
        if (answer_values == question_values):
            print(letters[i], "is a match!")
            # print_table(answer_values)

# values = check_all_values(question)
# print_table(values)
check_answers()
# print(my_function(False, True, False))
