def sequence(n):
    if n <= 0:
        return "Input a positive non-zero integer"
    elif n <= 4:
        return "Input an integer greater than 4"
    else:
        sequence_list = []
        while n > 0:
            sequence_list.append(str(n))
            n -= 1
    sequence_list.reverse()
    return "".join(sequence_list)
