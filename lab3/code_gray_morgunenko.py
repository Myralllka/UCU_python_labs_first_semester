def gray_code_number(number_input):
    return(number_input ^ (number_input >> 1))


def gray_uncode_number(number_input):
    number = number_input[0]
    for each in range(1, len(number_input)):
        number += str((int(number_input[each], 2) ^ int(number[each - 1], 2)))
    return(number)


gray_code_array = []
new_array = []
count = 0

for each in range(17, 28):
    gray_code_array.append("{0:05b}".format(
        int(bin(gray_code_number(each)), 2)))
    print(each, "\t" "=>", "{0:05b}".format(int(bin(each), 2)),
          "\t", "=>", "{0:05b}".format(int(bin(gray_code_number(each)), 2)), "\t", "=>", gray_uncode_number(gray_code_array[count]))
    count += 1
