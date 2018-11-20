number1, number2 = int(input("first_number:")), int(input("second_number:"))
xor = bin(number1 ^ number2)
sum = 0
length = len(xor)
for each in range(2, length):
    if xor[len(xor) - 1] == '1':
        sum += 1
    xor = str(bin(int(xor, 2) >> 1))
print(sum)
