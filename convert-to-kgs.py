def convert_to_kgs(lbs):
    kgs = round((lbs * 0.453592), 2)
    if lbs == 1 and kgs !=1:
        return f"{lbs} pound equals to {kgs} kilograms."
    elif kgs == 1 and lbs != 1:
        return f"{lbs} pounds equals to {kgs} kilogram."
    elif kgs == 1 and lbs == 1:
        return f"{lbs} pound equals to {kgs} kilogram."
    else:
        return f"{lbs} pounds equals to {kgs} kilograms."
