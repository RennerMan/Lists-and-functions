speeder_names = []
km_over_limit = []
tot_fine_amount = 0

def cost_finder(speed_over_limit):
    if speed_over_limit < 10:
        return 30
    elif 10 <= speed_over_limit <= 14:
        return 80
    elif 15 <= speed_over_limit <= 19:
        return 120
    elif 20 <= speed_over_limit <= 24:
        return 170
    elif 25 <= speed_over_limit <= 29:
        return 230
    elif 30 <= speed_over_limit <= 34:
        return 300
    elif 35 <= speed_over_limit <= 39:
        return 400
    elif 40 <= speed_over_limit <= 44:
        return 510
    elif speed_over_limit >= 45:
        return 630

while True:
    driver = input("What is the driver's name? (Type 'x' to quit)").lower()
    if driver == "x":
        break

    speed_over_limit = int(input(f"How many km was {driver} over the speed limit?"))

    if driver == "james wilson":
        print("WARRANT TO ARREST: James Wilson")
    elif driver == "helga norman":
        print("WARRANT TO ARREST: Helga Norman")
    elif driver == "zachary conroy":
        print("WARRANT TO ARREST: Zachary Conroy")

    cost = cost_finder(speed_over_limit)
    print(f"{driver} should be charged {cost}")
    speeder_names.append(driver)
    km_over_limit.append(speed_over_limit)
    tot_fine_amount += cost

print("Here are the speeder names:")
for driver in speeder_names:
    print(driver)
print("Here are how fast they went:")
for speed_over_limit in km_over_limit:
    print(speed_over_limit)
print(f"Total amount of fines: {tot_fine_amount}")
