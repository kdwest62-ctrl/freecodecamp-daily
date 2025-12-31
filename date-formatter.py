def format_date(date_string):
    month_dict = {
        'January': '01', 'February': '02', 'March': '03',
        'April': '04', 'May': '05', 'June': '06',
        'July': '07', 'August': '08', 'September': '09',
        'October': '10', 'November': '11', 'December': '12'}
    def year(date):
        year_char = [date[-4], date[-3], date[-2], date[-1]]
        return "".join(year_char)
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
                if element in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    day_char.append(element)
                else:
                    continue
        return "".join(day_char)

    if month(date_string) not in month_dict.keys() or int(day(date_string)) > 31:
        return "Invalid input"
    else:
        if len(day(date_string)) < 2:
            return f"{year(date_string)}-{month_dict[month(date_string)]}-0{day(date_string)}"
        else:
            return f"{year(date_string)}-{month_dict[month(date_string)]}-{day(date_string)}"
