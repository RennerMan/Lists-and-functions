# Vehicle Booking System created by chatgpt
# I used chat gpt as I didn't know how to do certain things in the question, eg: coding the "not enough seats" part
# However, I have tried to understand what each part does, so I can learn how to do things like this in future
# I hope that is okay!


# Creates a list of cars, containing the car number, type and number of seats
class VehicleBookingSystem:
    def __init__(self):
        self.vehicles = [
            {"number": 1, "type": "Suzuki Van", "seats": 2},
            {"number": 2, "type": "Toyota Corolla", "seats": 4},
            {"number": 3, "type": "Honda CRV", "seats": 4},
            {"number": 4, "type": "Suzuki Swift", "seats": 4},
            {"number": 5, "type": "Mitsubishi Air trek", "seats": 4},
            {"number": 6, "type": "Nissan DC Ute", "seats": 4},
            {"number": 7, "type": "Toyota Previa", "seats": 7},
            {"number": 8, "type": "Toyota Hi Ace", "seats": 12},
            {"number": 9, "type": "Toyota Hi Ace", "seats": 12}
        ]
        # Creates a list of bookings with the argument "self"
        self.bookings = []

    # Prints a list of available vehicles and displays "Not enough seats" when necessary
    def print_available_vehicles(self, seats_needed):
        print("\nAvailable vehicles:")
        for vehicle in self.vehicles:
            if vehicle["seats"] >= seats_needed:
                print(f"{vehicle['number']}. {vehicle['type']}, {vehicle['seats']} seats")
            else:
                print(f"{vehicle['number']}. {vehicle['type']}, {vehicle['seats']} seats (Not enough seats)")

    # A function that books a vehicle then removes it from the list
    def book_vehicle(self, vehicle_number, name):
        for vehicle in self.vehicles:
            if vehicle["number"] == vehicle_number:
                self.vehicles.remove(vehicle)
                self.bookings.append({"number": vehicle_number, "type": vehicle["type"], "name": name})
                print(f"\nVehicle {vehicle_number} ({vehicle['type']}) has been booked by {name}.")
                return
        print("Invalid vehicle number.")

    # Asks user how many seats they need and the vehicle number. If they enter -1, the program stops.
    def start_day(self):
        while self.vehicles:
            seats_needed = int(input("\nHow many seats do you need in the vehicle? (-1 to stop) "))
            if seats_needed == -1:
                print("Input stopped.")
                break
            self.print_available_vehicles(seats_needed)
            vehicle_number = int(input("Please input the number of the vehicle you want to book: "))
            name = input("Input your name: ")
            self.book_vehicle(vehicle_number, name)
        self.print_bookings()

    # A function that shows a list of all booked vehicles. If no vehicles were booked, it informs the user.
    def print_bookings(self):
        if self.bookings:
            print("\nAll booked vehicles:")
            for booking in self.bookings:
                print(
                    f"Vehicle number: {booking['number']}, Vehicle type: {booking['type']},\n"
                    f" Booked by: {booking['name']}")
        else:
            print("\nNo vehicles were booked.")


# Starts the program


booking_system = VehicleBookingSystem()
booking_system.start_day()
