def format_name(name_str):
    parts = name_str.split()

    # Check if there are at least two parts (first name and last name)
    if len(parts) >= 2:
        first_name = parts[0]
        last_name = parts[-1]  # Use the last part as the last name

    # Check if there are at least three parts (first, middle, last names)
    if len(parts) >= 3:
        middle_name = parts[1]
        middle_initial = middle_name[0]
        formatted_name = f"{last_name}, {first_name} {middle_initial}."
    else:
        formatted_name = f"{last_name}, {first_name}"

    return formatted_name
