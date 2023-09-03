import sys
from delivery_function import *


# The 'delivery_execution' function manages two delivery trips.
# It arranges packages, ensuring they're loaded onto trucks properly.
# It overseas the delivery of packages to their destinations. After each trip, it reports the completion status.
# It also handles updates like changing addresses and driver statuses.
# This function works with other functions in this program to execute the package deliveries.
def delivery_execution():
    # List of packages that must be loaded onto truck2
    packages_must_on_truck2 = [3, 18, 36, 38]

    # List of packages that must be loaded on the same truck
    packages_together = [13, 14, 15, 16, 19, 20]

    # List of packages that are delayed
    delayed_packages = [6, 9, 25, 28, 32]

    # Details for updating an address (package ID, new address, new zip code, time of change, address update boolean)
    address_update = [9, "410 S State St", 84111, "10:20", False]

    # Check if the user choice is 1 from the interactive menu at the beginning of this program
    # Then prints headline before listing deliveries for the first trip
    if int(user_choice) == 1:
        print("*****Trip No. 1*****")

    # Load trucks with packages for first trip using load_trucks function
    trucks_available_trip1 = load_trucks(packages_must_on_truck2, packages_together, delayed_packages)

    # Deliver packages using package_delivery function
    package_delivery(trucks_available_trip1, address_update, user_choice, update_address=True)

    # Check if the user choice is 1 from the interactive menu at the beginning of this program
    # Then reports trip completion
    if int(user_choice) == 1:
        print("Trip 1 is complete and trucks have returned to the hub")
        print()

    # Sets the driver status of truck 102 to "Off Duty"
    truck2.driver.status = "Off Duty"

    # Check if the user choice is 1 from the interactive menu at the beginning of this program
    # Then prints headline before listing deliveries for the second trip
    if int(user_choice) == 1:
        print("*****Trip No. 2*****")

    # Load trucks with remaining packages for the second trip using load_trucks function
    trucks_available_trip2 = load_trucks(packages_must_on_truck2, packages_together, delayed_packages)

    # Deliver remaining packages using the package_delivery function
    package_delivery(trucks_available_trip2, address_update, user_choice, update_address=True)

    # Check if the user choice is 1 from the interactive menu at the beginning of this program
    if int(user_choice) == 1:
        print("All deliveries have been completed and trucks have returned to the hub")
        print()


# The 'check_delivery_status' function checks the delivery status of packages at a specified time.
# It iterates through the packages in the package container hashtable and examines each package's delivery history and status.
# It determines whether a pacakge is at the hub, en route, or delivered based on its status and delivery time.
# It updates the status of packages accordingly and calculates the miles travelled by the trucks based on the specified time.
def check_delivery_status(specified_time):

    # If truck1 has no delivered packages
    if not truck1.package_info:
        # Find the latest time truck1 returned to the hub
        max_index1 = truck1.last_time_returned_hub.index(max(truck1.last_time_returned_hub))

        # Adjust the specified time if it's later than the latest return time
        if specified_time > truck1.last_time_returned_hub[max_index1].time():
            specified_time = truck1.last_time_returned_hub[max_index1].time()

        # Calculate miles travelled by truck1 based on adjusted time
        truck1.miles_travelled = (18 * ((specified_time.hour - 8) + (specified_time.minute / 60)))

    # Loop through the package container hashtable buckets
    for bucket_list in package_container.table:
        # Loop through package data in each bucket
        for package_data in bucket_list:
            # Get the package object from package data
            pac_kage = package_data[1]

            # Check if the package's ID is in the list of delivered packages for each truck
            for truck in [truck1, truck2, truck3]:
                if pac_kage.p_id in truck.id_of_package_delivered:
                    truck = truck
                    break

            # Find the earliest and latest return times for the truck
            min_index = truck.last_time_returned_hub.index(min(truck.last_time_returned_hub))
            max_index = truck.last_time_returned_hub.index(max(truck.last_time_returned_hub))

            # Extract delivery time from package status
            if "*****Delayed*****" in pac_kage.p_status:
                delivery_time_str = pac_kage.p_status.split(" ")[-3]
            else:
                delivery_time_str = pac_kage.p_status.split(" ")[-2]

            # Convert delivery time to a datetime object
            delivery_time = datetime.strptime(delivery_time_str, '%H:%M').time()
            delivery_datetime = datetime.combine(datetime.today(), delivery_time)

            # Compare the actual delivery time with the specified time
            # Update package status based on comparison
            if delivery_datetime.time() <= specified_time:
                continue
            else:
                if delivery_datetime.time() > truck.last_time_returned_hub[min_index].time() > specified_time:
                    pac_kage.p_status = "At Hub"
                else:
                    pac_kage.p_status = "En Route"

            # Compares the specified time with the earliest and latest time a truck returned to the hub after deliveries.
            # This comparison is used to calculate the actual cumulative mileage traveled by a truck as of a specified time.
            if truck.last_time_returned_hub[max_index].time() >= specified_time >= truck.last_time_returned_hub[min_index].time():
                truck.miles_travelled = (18 * ((specified_time.hour - 8) + (specified_time.minute / 60)))
            elif truck.last_time_returned_hub[max_index].time() >= specified_time >= truck.last_time_returned_hub[min_index].time():
                truck.miles_travelled = (18 * ((truck.last_time_returned_hub[max_index].hour - 8) + (truck.last_time_returned_hub[max_index].minute / 60)))
            else:
                truck.miles_travelled = (18 * ((specified_time.hour - 8) + (specified_time.minute / 60)))


input_time = None  # Initialize input_time with None

# The print statement below provide a user interface for the Parcel Management System.
# Users are offered 4 options to choose from.
print("PARCEL MANAGEMENT SYSTEM")
print("Good Day, what would you like to do here today?")
print("1.) Get total mileage after delivering all packages")
print("2.) Check the status of packages at a certain time")
print("3.) Check the status of an individual package at a certain time")
print("4.) Exit")
print("Type integer 1, 2, 3 or 4:")

# This while loop below repeatedly prompts the user for input. If the input is not 1, 2, 3 or 4, an error message is shown.
# Once a valid input is received, the loop terminates, ensuring only valid choices are accepted.
while True:
    user_choice = input()

    if user_choice not in ('1', '2', '3', '4'):
        print("Error: Please enter either 1, 2, 3 or 4.")
    else:
        break  # Valid input, exit the loop

# In the interactive menu if the user choice is 1, it initiates the package delivery using the delivery_execution function.
# After all the packages are delivered, it retrieves and displays the status of each package by iterating through them.
# It also calculates and prints the total combined mileage of all three trucks for the day.
if int(user_choice) == 1:

    # execute the delivery process
    delivery_execution()

    print("Status After all the Packages have been Delivered:")
    for pack in range(1, 41):
        pack_info = package_container.get_package(pack)
        print(pack_info)

    print()
    total_mileage = truck1.miles_travelled + truck2.miles_travelled + truck3.miles_travelled
    print("Combined mileage of all trucks for the day: ", total_mileage)


# In the interactive menu if the user choice is 2, the user is asked to input a time in 24 hours format.
# The time entered by the user is checked for validity. It repeatedly aks for an input until a valid time is entered.
# The code then initiates the package delivery using the delivery_execution function.
# If the input time is before 10:20 am, package 9's address and zipcode are updated.
# check_delivery_status is used to assess package delivery status.
# Then the information of all the packages is displayed with the status up to the specified time.
# The code also display the combined mileage of all trucks up to the specified time.
if int(user_choice) == 2:
    print("Enter a time in format HH:MM:")

    # checks if the input time is valid
    while True:
        user_input = input()
        try:
            input_time = datetime.strptime(user_input, '%H:%M').time()
            if input_time < time(8, 0):
                print("Error: Time cannot be earlier than 08:00. Please enter a valid time.")
            else:
                break  # Valid input, exit the loop
        except ValueError:
            print("Error: Invalid time format. Please enter a time in format HH:MM")
            continue  # Go back to the start of the loop to ask for input again

    # execute the delivery process
    delivery_execution()

    # if the time is less than 10:20 am, the address and zipcode for package 9 are updated
    if input_time is not None:
        if input_time < time(10, 20):
            package = package_container.get_package(9)
            if package is not None:
                package.p_address = "300 State St"
                package.p_zipcode = 84103

        # check_delivery_status function is used to check the status of all packages up to the input time.
        check_delivery_status(input_time)
        print()

        # information and status of all packages are printed
        print(f"Delivery Status of All Packages at {input_time.strftime('%I:%M %p')}:")
        for pkg in range(1, 41):
            package_info = package_container.get_package(pkg)
            print(package_info)

    # Displays total combined mileage of all trucks up to the specified time
    print()
    total_mileage = truck1.miles_travelled + truck2.miles_travelled + truck3.miles_travelled
    print(f"Combined mileage of all trucks at {input_time.strftime('%I:%M %p')}: {total_mileage}")


# In the interactive menu if the user choice is 3, the user is asked to input a package ID followed by a time in 24 hours format.
# User inputs are validated. The code prompts the user repeatedly until a valid input is received.
# The packaged ID is validated by iterating through all the packages in the hashtable.
# The code then initiates the package delivery using the delivery_execution function.
# If the input time is before 10:20 am, package 9's address and zipcode are updated.
if int(user_choice) == 3:
    print("Enter a package ID:")

    # checks if the package ID is an integer and matches the ID with one of the packages in the hashtable.
    while True:
        integer_package_id = False  # Start with False
        user_input_package_id = input()
        try:
            user_input_package_id = int(user_input_package_id)
            integer_package_id = True  # Set to True when a valid integer is entered
        except ValueError:
            print("Error: Please enter a valid integer for the package ID.")

        # if the input is an integer
        if integer_package_id:
            package_found = False  # Flag to indicate if a valid package is found

            # iterates through all the packages in the hashtable until a package ID match is found
            for bkt_list in package_container.table:
                for data in bkt_list:
                    if user_input_package_id == data[0]:
                        package_found = True
                        break  # Package ID found, exit the loop

                if package_found:
                    break  # Exit the outer loop as well if package found

            # prints a message if the package is found or otherwise
            if package_found:
                print("Package found!")
                break  # Exit the main loop
            else:
                print("Error: Please enter a valid package ID.")

    # asks the user to input a time in 24 hours format
    print("Enter a time in format HH:MM:")

    # check the if the time entered by the user is valid
    while True:
        user_input_time = input()
        try:
            input_time = datetime.strptime(user_input_time, '%H:%M').time()
            if input_time < time(8, 0):
                print("Error: Time cannot be earlier than 08:00. Please enter a valid time.")
            else:
                break  # Valid input, exit the loop
        except ValueError:
            print("Error: Invalid time format. Please enter a time in format HH:MM")
            continue  # Go back to the start of the loop to ask for input again

    # execute the delivery process
    delivery_execution()

    # if the time is less than 10:20 am, the address and zipcode for package 9 are updated
    if input_time is not None:
        if input_time < time(10, 20) and int(user_input_package_id) == 9:
            package = package_container.get_package(int(user_input_package_id))
            if package is not None:
                package.p_address = "300 State St"
                package.p_zipcode = 84103

        # information and status of all packages are printed
        check_delivery_status(input_time)
        print()

        # information and status is displayed for the package with the package ID entered by the user
        print(f"Delivery Status of Package ID: {user_input_package_id} at {input_time.strftime('%I:%M %p')}:")
        print(package_container.get_package(int(user_input_package_id)))


# In the interactive menu if the user choice is 4, the program exits.
if int(user_choice) == 4:
    sys.exit()
