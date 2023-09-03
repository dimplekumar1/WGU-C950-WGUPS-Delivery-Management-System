from datetime import datetime, timedelta, time
from package_data import *
from distance_data import *


mileage_data = load_mileage('mileage_table.csv')  # loads data distance data form external csv file


# This function takes two inputs: a package_info list and a delivery address.
# It goes through the package_info list, checking if the delivery address matches the address of each package.
# If there is a match, the package data is added to a new list called delivered_packages.
# Finally, the function returns this list (delivered_packages) containing all packages delivered to the specified address.
def get_delivered_packages(package_info, delivery_address):
    delivered_packages = []
    for package_data in package_info:
        if package_data[1].p_address == delivery_address:
            delivered_packages.append(package_data)
    return delivered_packages


# This function facilitates the updating of a package's delivery status.
# It accepts package data containing package ID and object, as well as a status string indicating the new delivery status.
# Using package_container hashtable, the function assess the relevant information and invokes the update_package_status_by_id method to modify the delivery status.
def update_package_delivery(package_data, status):
    package_id, pac = package_data
    package_container.update_package_status_by_id(pac.p_id, pac.p_address, status)


# This function takes two inputs: package_data and estimate_delivery_time.
# The purpose of this function is to display a correct delivery status of a package.
# It checks if the estimated delivery time is past the package's deadline, and if so, it appends "Delayed" to the status string.
# Finally, it calls another function update_package_delivery to update package's delivery status by passing package_data and computed status as parameters.
def update_package_delivery_status(package_data, estimated_delivery_time):
    status = f"Delivered at {estimated_delivery_time.strftime('%I:%M %p')}"
    if package_data[1].p_deadline != "EOD" and estimated_delivery_time.strftime('%I:%M %p') > package_data[1].p_deadline:
        status = f"Delivered at {estimated_delivery_time.strftime('%I:%M %p')} *****Delayed*****"
    update_package_delivery(package_data, status)


# This function is responsible for computing and updating the distance travelled by a given truck during its travel from current location to a target address.
# It retrieves distance indices for both locations from the distanceData hashtable and loads the distance data form the external csv file.
# By using get_distance_between_two_locations function, it determines the distance covered. Then distance is added to the trucks accumulated mileage.
def update_mileage(truck, current_location, target_address):
    distance_from = distanceData.distance_id(current_location) - 1  # current location
    distance_to = distanceData.distance_id(target_address) - 1  # target location
    distance_traveled = get_distance_between_two_locations(mileage_data, distance_from, distance_to)   # travel distance calculation between two locations
    truck.miles_travelled += distance_traveled  # adding the travelled distance to the accumulated mileage
    return distance_traveled


# This function estimates the time needed for package delivery by considering the distance to be covered and the current time.
# It calculates the required time using assumed travel speed of 18 miles per hour by using the timedelta class for time duration manipulation.
# The calculated delivery time is then added to the current time to get the estimated time for the package delivery.
def package_delivery_time(distance, current_time):
    time_to_deliver = timedelta(hours=distance / 18)
    current_time += time_to_deliver
    return current_time


# This function handles the address update process for packages in transit on a delivery trucks route.
# It checks if an address update has already been processed for a package using a flag/boolean in the provided address_update list.
# If not, the function calculates the estimated mileage at the update time and compares it to the truck's traveled distance.
# If the conditions are met, the function updates the package's address and zipcode.
def update_package_address(truck, address_update, user_choice):

    # Check if the address has already been updated for this package
    if address_update[4]:
        return

    update_time = datetime.strptime(address_update[3], '%H:%M')
    # Estimate the mileage based on the update time
    mileage_at_update_time = (18 * ((update_time.hour - 8) + (update_time.minute / 60)))

    # Compares if the mileage at the update time is less than or equal to the truck's accumulated mileage
    if mileage_at_update_time <= truck.miles_travelled:
        # The print statement is only displayed if the use choice is one at the beginning of the program.
        if int(user_choice) == 1:
            print("*****Address update for a package*****")

        # Iterates through all the packages in the truck until a matching package ID is found
        # Then updates the package address
        for p_data in truck.package_info:
            if p_data[0] == address_update[0]:
                package_data = p_data
                package_data[1].p_address = address_update[1]
                package_data[1].p_zipcode = address_update[2]
                # The print statement is only displayed if the use choice is one at the beginning of the program.
                if int(user_choice) == 1:
                    print(f"Package {address_update[0]} address updated to {package_data[1].p_address}")
                # Set the flag to indicate the update has been applied
                address_update[4] = True
                break


# Nearest Neighbor Algorithm
# This function is the core of this program, responsible for simulating package deliveries using a list of trucks.
# For each truck, this function iteratively matches packages with their corresponding delivery addresses.
# It calculates distance, estimates delivery times, and updates package delivery statuses.
# This function employs a Nearest Neighbor Algorithm to optimize delivery route planning.
# By utilizing distanceData.nearest_distances_sorted function, it sorts delivery address by proximity to the current location.
# It also ensures that the packages in a truck with the same delivery address are delivered at the same time.
def package_delivery(truck_list, address_update, user_choice, update_address):
    hub_location = "4001 S 700 E"  # hub location address
    base_time = datetime.combine(datetime.today(), time(8, 0))  # delivery start time: 08:00 am

    # Iterate through all trucks
    for truck in truck_list:  # Time Complexity: O(n)
        current_location = hub_location  # set current location to the hub location to start delivery
        #  This if statement ensures that if this is the second trip for a particular truck, the time accumulates. Otherwise, sets the time to 08:00 am.
        if not truck.last_time_returned_hub:
            estimated_delivery_time = base_time
        else:
            estimated_delivery_time = truck.last_time_returned_hub[0]

        # The print statement is only displayed if the use choice is one at the beginning of the program.
        if int(user_choice) == 1:
            print(f"Delivering packages for Truck {truck.truck_id}:")

        # The while loop checks if there are packages in a truck before starting delivering the packages
        while truck.package_info:
            sorted_delivery_addresses = distanceData.nearest_distances_sorted(current_location)  # this sorts delivery addresses by proximity to the current location. # Time Complexity: O(n^4)
            delivered_package = None

            # Loops through all addresses in the sorted delivery addresses until a match is found with the package address in the truck
            for delivery_address in sorted_delivery_addresses:
                # This function provides a list containing all packages with a first matching address in sorted_delivery_addresses
                delivered_packages = get_delivered_packages(truck.package_info, delivery_address)

                # Iterates through all packages in delivered_packages list
                for package_data in delivered_packages:
                    delivered_package = package_data
                    delivery_address = package_data[1].p_address
                    distance_traveled = update_mileage(truck, current_location, delivery_address)  # distance calculation to accumulate mileage
                    estimated_delivery_time = package_delivery_time(distance_traveled, estimated_delivery_time)  # time calculation and accumulation

                    update_package_delivery_status(package_data, estimated_delivery_time)  # updates status after package delivery

                    truck.num_package_delivered += 1  # keeps track of number of packages delivered
                    truck.package_info.remove(package_data)  # removes the package from the truck after delivery
                    current_location = delivery_address  # After delivery, the current location is set to the recent package delivery location

                    if update_address:
                        update_package_address(truck, address_update, user_choice)  # updates the address for a specific package en-route

                    # The print statement is only displayed if the use choice is one at the beginning of the program.
                    if int(user_choice) == 1:
                        print(
                            f"Truck: {truck.truck_id}, Package: {package_data[1].p_id}, Distance: {distance_traveled} miles from {current_location} to {delivery_address}. Cumulative mileage: {truck.miles_travelled: .2f} miles. Delivery Time: {estimated_delivery_time.strftime('%I:%M %p')}")

                if delivered_package:
                    break  # Break the inner loop when packages are delivered

            if not delivered_package:
                print("No more matching packages for remaining addresses.")
                break

        # The print statements are only displayed if the use choice is one at the beginning of the program.
        if int(user_choice) == 1:
            print()
            print(f"Remaining packages in Truck {truck.truck_id}:")
            # This check is in place to see if all packages are delivered or not.
            # If there are no more packages in the truck, it prints None, otherwise, it prints all the remaining packages to be delivered.
            if not truck.package_info:
                print("None")
            else:
                for package_data in truck.package_info:
                    print(package_data[0], package_data[1].p_address)
            print()

        # Now the truck is returning to the hub
        distance_traveled = update_mileage(truck, current_location, hub_location)  # distance calculation and accumulation for travelling back to hub
        estimated_delivery_time = package_delivery_time(distance_traveled, estimated_delivery_time)  # time calculation and accumulation for travelling back to hub
        truck.last_time_returned_hub.append(estimated_delivery_time)  # This appends the time at truck is returned to the hub to a dedicated list

        # The print statement is only displayed if the use choice is one at the beginning of the program.
        # Print statement confirms that the truck is returning to the hub and prints cumulative mileage and current time
        if int(user_choice) == 1:
            print(
                f"Truck {truck.truck_id} is returning to the hub. Cumulative mileage for this truck: {truck.miles_travelled: .2f} miles. Time Returned to the hub: {estimated_delivery_time.strftime('%I:%M %p')}")
            print()
