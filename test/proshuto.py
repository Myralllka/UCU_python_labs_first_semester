def input_std():
    res = []
    while True:
        text = input("print here name, (enter to continue) weidth and cost: ")
        if not text:
            break
        text = text.split()
        text[1], text[2] = int(text[1]), int(text[2])
        res.append(text)
    return res


if __name__ == "__main__":
    line = input_std()
    line = sorted(line, key=lambda x: x[2] / x[1])
    print(line)
