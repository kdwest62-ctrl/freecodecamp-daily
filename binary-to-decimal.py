def to_decimal(binary):
    num_list = []
    exp = len(str(binary)) - 1
    for item in str(binary):
        num = int(item) * (2 ** exp)
        num_list.append(num)
        exp -= 1
    return sum(num_list)
