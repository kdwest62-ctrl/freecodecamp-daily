def to_roman(num):
    if num > 1000 or num <= 0:
        return "Conversion not available"
    else:
        dict1 = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        dict2 = {2: 'II', 3: 'III', 4: 'IV', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
        dict3 = {20: 'XX', 30: 'XXX', 40: 'XL', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC'}
        dict4 = {200: 'CC', 300: 'CCC', 400: 'CD', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM'}
        if num in dict1.keys():
            return dict1[num]
        elif num in dict2.keys():
            return dict2[num]
        elif num in dict3.keys():
            return dict3[num]
        elif num in dict4.keys():
            return dict4[num]
        else:
            if len(str(num)) == 3:
                numbers = []
                roman_char = []
                string_num = str(num)
                num1, num2, num3 = string_num[0] + '00', string_num[1] + '0', string_num[2]
                numbers.append(int(num1))
                numbers.append(int(num2))
                numbers.append(int(num3))
                for item in numbers:
                    if item in dict1.keys():
                        roman_char.append(dict1[item])
                    elif item in dict2.keys():
                        roman_char.append(dict2[item])
                    elif item in dict3.keys():
                        roman_char.append(dict3[item])
                    elif item in dict4.keys():
                        roman_char.append(dict4[item])
                    else:
                        continue
                return "".join(roman_char)
            elif len(str(num)) == 2:
                numbers = []
                roman_char = []
                string_num = str(num)
                num1, num2 = string_num[0] + '0', string_num[1]
                numbers.append(int(num1))
                numbers.append(int(num2))
                for item in numbers:
                    if item in dict1.keys():
                        roman_char.append(dict1[item])
                    elif item in dict2.keys():
                        roman_char.append(dict2[item])
                    elif item in dict3.keys():
                        roman_char.append(dict3[item])
                    elif item in dict4.keys():
                        roman_char.append(dict4[item])
                    else:
                        continue
                return "".join(roman_char)
            else:
                return "Invalid length"
