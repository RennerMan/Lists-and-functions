child_name = []


def drop_off():
    name = input("What is your child's name? ")
    child_name.append(name)
    print(f"{name} was added to the roll")


def pick_up():
    name = input("What is your child's name? ")
    if name in child_name:
        child_name.remove(name)
        print(f"{name} has been checked out.")
    else:
        print(f"Error: There is no child named {name} in the daycare.")


def calc_cost():
    hours = int(input("How many hours are the children at the daycare for? "))
    cost = hours * 12 * len(child_name)
    print(f"The charge of having {len(child_name)} children at the daycare for {hours} hours\n "
          f"is ${cost}. ")


def print_roll():
    roll = input("Do you wish to print a roll of all children in the daycare? (y/n)").lower()
    if roll == "yes" or roll == "y":
        for child in child_name:
            print(child)
        if len(child_name) == 0:
            print("There are no children in the roll!")

    elif roll == "no" or roll == "n":
        pass
    else:
        print("Your answer wasn't yes or no! please enter again.")


choice = 0

while choice != 5:
    print("-----------------------------------------------------------------------")
    print("                      Welcome to MGS Childcare")
    print("-----------------------------------------------------------------------")

    print("What would you like to do? Please choose one of the items below")
    print()
    print("1 Drop off a child")
    print()
    print("2 Pick up a child")
    print()
    print("3 Calculate cost")
    print()
    print("4 Print roll")
    print()
    print("5 Exit the system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()
    if choice == 1:
        drop_off()

    elif choice == 2:
        pick_up()

    elif choice == 3:
        calc_cost()

    elif choice == 4:
        print_roll()

    elif choice == 5:
        print("Goodbye")

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
