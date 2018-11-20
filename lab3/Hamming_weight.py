for i in range(21):
    hamming_weight, odious, val = 0, False, ""
    binary = bin(5 ** i)
    for each in binary:
        if (each == "1"):
            hamming_weight += 1
    if (hamming_weight % 2 == 1):
        odious = True
    if (odious):
        val = "odious"
    else:
        val = "evil"
    print("5 **", str(i) + '\t'"=", hamming_weight, "\t", ":", val)
