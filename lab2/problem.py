array_prime = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
try:
    number = int(input())
except ValueError:
    print("Error")
else:
    if number < 3:
        print("Error")
    else:
        for each in array_prime:
            if number % each != 0:
                print(each)
                break
