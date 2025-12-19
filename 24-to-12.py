def to_12(time):
    if len(time) < 4 or len(time) > 4:
        return "Invalid length"
    else:
        minute_check = []
        for item in time:
            minute_check.append(int(item))
        if minute_check[2] >= 6:
            return "Error: minutes must be less than 60"
        else:
            if time == "0000":
                return "12:00 AM"
            elif 0 < int(time) < 1200:
                if int(time) < 100:
                    return f"12:{time[2]}{time[3]} AM"
                else:
                    return f"{time[0]}{time[1]}:{time[2]}{time[3]} AM"
            elif time == "1200":
                return "12:00 PM"
            elif 1200 < int(time) < 2359:
                t = str(int(time) - 1200)
                if len(t) == 4:
                    return f"{t[0]}{t[1]}:{t[2]}{t[3]} PM"
                elif len(t) == 3:
                    return f"0{t[0]}:{t[1]}{t[2]} PM"
                elif len(t) == 2:
                    return f"12:{t[0]}{t[1]} PM"
                else:
                    return f"12:0{t[0]} PM"
            elif time == "2359":
                return "11:59 PM"
            elif time == "2400":
                return "2400 is just the same as 0000"
            else:
                return "Invalid time"
