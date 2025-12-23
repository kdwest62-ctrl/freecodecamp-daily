def to_binary(num):
    binary_list = []
    while True:
        a = num // 2
        b = num % 2
        binary_list.append(str(b))
        if a == 0:
            break
        else:
            del num
            num = a
            del a, b
    binary = "".join(binary_list)
    return binary[::-1]
