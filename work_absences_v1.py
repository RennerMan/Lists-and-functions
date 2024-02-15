employee_names = []
employee_name = ""
most_absences = 0
while employee_name != "$":
    employee_name = input("What is the employee's name?")
    absence_days = int(input("How many days were they absent for?"))
    employee_names.append(employee_name + absence_days)
    if absence_days > most_absences:
        most_absences = absence_days

