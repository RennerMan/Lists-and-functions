trip_details = []
tot_time = 0
preferred_decimal_places = 2

driver_name = input("What is the driver's name?")
new_trip = input("Do you want to start a new trip? (yes/no)").lower()

while new_trip != "no":
    if new_trip == "yes" or new_trip == "y":
        time = int(input("How long did the trip take? (minutes)"))
        tot_time += time  # Update total time
        cost = 10 + 2 * time
        trip_details.append(time + cost)
    else:
        print("You didn't say yes or no! Try again.")
    new_trip = input("Do you want to start a new trip? (yes/no)").lower()

print(f"The driver's name is {driver_name}")
print(f"The total time is {tot_time} minutes")
if trip_details:
    average_time = sum(trip_details) / len(trip_details)
    print(f"The average time is {average_time:.{preferred_decimal_places}f} minutes")
else:
    print("No trips recorded.")
