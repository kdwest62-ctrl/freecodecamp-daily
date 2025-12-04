import string

def digits_or_letters(s):
    def digits(st):
        digits_list = []
        for item in st:
            if item in string.digits:
                digits_list.append(item)
        return len(digits_list)
    def letters(st):
        letters_list = []
        for item in st:
            if item in string.ascii_letters:
                letters_list.append(item)
        return len(letters_list)
    if digits(s) > letters (s):
        return "digits"
    elif letters(s) > digits(s):
        return "letters"
    else:
        return "tie"
