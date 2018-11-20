input_number = input()
pair = len(input_number) // 2 + 1
if (len(input_number) % 2 == 0):
    pair -= 1
result = 0
for each in range(pair):
    one = input_number[-each - 1]
    two = input_number[each]
    if (two == one):
        result += 1

print(result)
