def most_frequent(arr):
    test_arr = []
    frequent_arr = []
    for item in arr:
        if item not in test_arr:
            test_arr.append(item)
        else:
            frequent_arr.append(item)
    if len(frequent_arr) == 0:
        return "nothing frequent"
    else:
        return f"{set(frequent_arr)}"
