employeeNames = []
employeeDaysAbsent = []


def float_test(input_prompt):
    error_message = "Please enter a valid float. Try again."
    while True:
        try:
            number = float(input(input_prompt))
            return number
        except ValueError:
            print(error_message)


def highest_list_value_index(number_list):
    highest_value = 0
    highest_value_index = 0
    for i, value in enumerate(number_list):
        if value > highest_value:
            highest_value = value
            highest_value_index = i
    return highest_value_index


def int_test(input_prompt):
    error_message = "Please enter a valid integer. Try again."
    while True:
        try:
            number = int(input(input_prompt))
            return number
        except ValueError:
            print(error_message)


def average_list_value(float_list, decimal_places):
    list_sum = sum(float_list)
    average = list_sum / len(float_list)
    average_rounded = round(average, decimal_places)
    return average_rounded


def ask_for_employee_names():
    number_of_employees = int_test("How many employees are there? ")
    i = 1
    print("")
    while i <= number_of_employees:
        name = input(f"Input the name for employee #{i}: ").capitalize()
        employeeNames.append(name)
        i += 1


def ask_for_days_absent():
    print("")
    for employee in employeeNames:
        days_absent = int_test(f"How many days has {employee} been absent this year? ")
        employeeDaysAbsent.append(days_absent)


def initial_input():
    ask_for_employee_names()
    if employeeNames:
        ask_for_days_absent()


def print_employees_always_present():
    number_present = 0
    always_present_list = []
    print("\nEmployees always present: (sorted alphabetically)")

    for i, days_absent in enumerate(employeeDaysAbsent):
        if days_absent == 0:
            always_present_list.append(employeeNames[i])
            number_present += 1

    always_present_list = sorted(always_present_list) # Alphabetical order

    for i, always_present_name in enumerate(always_present_list):
        print(f"{i + 1}. {always_present_name}")

    if number_present == 0:
        print("(No employees have been always present)")
    elif number_present == 1:
        print("(1 employee has been always present)")
    else:
        print(f"({number_present} employees are always present)")


def print_employees_above_average_absence(average_value):
    number_above_average = 0
    above_average_name_list = []
    above_average_value_list = []
    print("\nEmployees with above average absences: (sorted alphabetically)")

    for i, days_absent in enumerate(employeeDaysAbsent):
        if days_absent > average_value:
            above_average_name_list.append(employeeNames[i])
            above_average_value_list.append(days_absent)
            number_above_average += 1

    above_average_name_list = sorted(above_average_name_list)  # Alphabetical order

    for i, above_average_name in enumerate(above_average_name_list):
        print(f"{i + 1}. {above_average_name} ({above_average_value_list[i]} days absent)")


def print_stats():
    average_days_absent = average_list_value(employeeDaysAbsent, 1)
    most_absent_index = highest_list_value_index(employeeDaysAbsent)
    most_absence_name = employeeNames[most_absent_index]
    most_days_absent = employeeDaysAbsent[most_absent_index]
    print("")
    print(f"The average days absent this year is {average_days_absent}")
    print(f"The most days absent is {most_days_absent} days by {most_absence_name}")
    print_employees_always_present()
    print_employees_above_average_absence(average_days_absent)


def start():
    initial_input()
    if employeeNames:
        print_stats()
    else:
        print("No employees to print statistics for!")


start()
