def number_of_files(file_size, file_unit, drive_size_gb):
    if file_unit == "b" or file_unit == "B":
        return (1000000000 / file_size) * drive_size_gb
    elif file_unit == "kb" or file_unit == "KB":
        return (1000000 / file_size) * drive_size_gb
    elif file_unit == "mb" or file_unit == "MB":
        return (1000 / file_size) * drive_size_gb
    else:
        return "Incorrect file unit"
