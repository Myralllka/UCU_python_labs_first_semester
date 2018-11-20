import random


def surname_num(lst):
    '''
    (list) -> None
    Print in file surnames with random numbers
    '''
    result = ""
    for each in lst:
        result += each + str(random.randint(1, 9)) + "\n"

    with open("surnames.txt", "w") as output_file:
        print(result, file=output_file, end="")


print(surname_num(["a", "b", "c", "ad"]))