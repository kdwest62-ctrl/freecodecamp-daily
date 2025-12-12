import string

def format_date(date_string):
    def month(date):
        month_char = []
        for item in date:
            if item == " ":
                break
            else:
                month_char.append(item)
        return "".join(month_char)
    def day(date):
        day_char = []
        for element in date:
            if element == ",":
                break
            else:
                if element in string.digits:
                    day_char.append(element)
                else:
                    continue
        return "".join(day_char)
    def year(date):
        year_char = [date[-4], date[-3], date[-2], date[-1]]
        return "".join(year_char)
    if len(month(date_string)) > 2:
        if len(day(date_string)) < 2:
            return f"{year(date_string)}-{month(date_string)}-0{day(date_string)}"
        else:
            return f"{year(date_string)}-{month(date_string)}-{day(date_string)}"
    else:
        return "Input full name of the month"
