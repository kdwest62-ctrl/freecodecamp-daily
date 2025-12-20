def to_decimal(binary):
    binary_check = []
    for item in str(binary):
        if item != "0" and item != "1":
            binary_check.append(item)
        else:
            continue
    if len(binary_check) != 0:
        return "A binary number can only be made up of 0's and 1's"
    else:
        num_list = []
        exp = len(str(binary)) - 1
        for item in str(binary):
            num = int(item) * (2 ** exp)
            num_list.append(num)
            exp -= 1
        return sum(num_list)
