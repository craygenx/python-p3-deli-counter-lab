def now_serving_with_empty_line(katz_deli):
    if not katz_deli:
        return "The line is currently empty."
    else:
        line_status = "The line is currently:"
        for idx, person in enumerate(katz_deli, start=1):
            line_status += f" {idx}. {person}"
        return line_status

def take_a_number_multiple_times(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    return f"Welcome, {name}. You are number {position} in line."

def now_serving_with_people_in_line(katz_deli):
    if not katz_deli:
        return "There is nobody waiting to be served!"
    else:
        serving_person = katz_deli.pop(0)
        return f"Currently serving {serving_person}."