number = int(input())
input_number = number // 100
epact = (8 + (input_number // 4) - input_number +
         ((8 * input_number + 13) // 25) + 11 * (number % 19)) % 30
print(epact)
