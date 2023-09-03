import csv
from models import *


# This class initializes a hash table to store package data
# HashTable class using chaining.
class PackageDataHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for k in range(initial_capacity):
            self.table.append([])

    # Inserts and update a new item into the hash table.
    def insert(self, package_id, pac_info):
        # get the bucket list where this item will go.
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # update if item already in the bucket
        for pac in bucket_list:
            # print key_value
            if pac[0] == package_id:
                pac[1] = pac_info
                return True

        # Insert the data into the bucket
        package_data = [package_id, pac_info]
        self.table[bucket].append(package_data)
        return True

    # This function facilitates the retrieval of packages information from the hash table using a given package ID.
    # It navigates through the hash table's buckets and the package data within them.
    # It compares the provided package ID with the package ID in each bucket list.
    # Once the matching package ID is found, the function returns corresponding package data.
    def get_package(self, package_id):
        # get the bucket list
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]
        # get the item from the bucket list if present
        for package_data in bucket_list:
            if package_data[1].p_id == package_id:
                return package_data[1]

    # Remove an item from the hash table
    def remove(self, package_id):
        # get the bucket list where this item will be removed from.
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for pac in bucket_list:
            # print key_value
            if pac[0] == package_id:
                bucket_list.remove([pac[0], pac[1]])

    # This function is responsible for modifying the delivery status of a package in the hash table.
    # It searches through the hash table's buckets to find the package data associated with a specific package ID and address.
    # Once a match is found, the function updates the package's status attribute.
    def update_package_status_by_id(self, package_id, package_address, status):
        # get the bucket list
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]
        # search for the key in the bucket list
        for package_data in bucket_list:
            if package_data[1].p_id == package_id and package_data[1].p_address == package_address:
                package_data[1].p_status = status


# This class initializes a hash table to store package data
# HashTable class using chaining.
class PackageUpdaterHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for k in range(initial_capacity):
            self.table.append([])

    # Inserts and update a new item into the hash table.
    def insert(self, package_id, pac_info):
        # get the bucket list where this item will go.
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # update if item already in the bucket
        for pac in bucket_list:
            # print key_value
            if pac[0] == package_id:
                pac[1] = pac_info
                return True

        # Insert the data into the bucket
        package_data = [package_id, pac_info]
        self.table[bucket].append(package_data)
        return True

    # Removes an item with matching key from the hash table.
    def remove(self, package_id):
        # get the bucket list where this item will be removed from.
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for pac in bucket_list:
            # print key_value
            if pac[0] == package_id:
                bucket_list.remove([pac[0], pac[1]])


# This function reads through package details from a CSV file.
# It iterates through each row, extracting the relevant information.
# This information is then inserted into both hash tables.
def load_package_data(package_file):
    with open(package_file) as package_file:
        package_data = csv.reader(package_file, delimiter=',')
        next(package_data)  # skip header
        for pac in package_data:
            package_id = int(pac[0])
            package_address = pac[1]
            package_city = pac[2]
            package_zipcode = pac[3]
            package_deadline = pac[4]
            package_weight = pac[5]
            package_status = "At Hub"

            # package object
            pac_info = Package(package_id, package_address, package_deadline, package_city, package_zipcode, package_weight, package_status)
            # print(package_info)

            # insert it into the hash tables
            package_container.insert(package_id, pac_info)
            package_updates.insert(package_id, pac_info)


# This function extracts and returns zip code of a given package data.
def get_delivery_zipcode(package_data):
    return package_data[1].p_zipcode


# Initialize package_info list and define the size for each truck object
package_info_truck1 = [] * 16
package_info_truck2 = [] * 16
package_info_truck3 = [] * 16

# Initialize package_id list for each truck object
package_ids1 = []
package_ids2 = []
package_ids3 = []

# Initialize time_returned_hub list for each truck object
time_returned_hub1 = []
time_returned_hub2 = []
time_returned_hub3 = []

# Initialize driver objects
driver1 = Drivers(1, "On Duty")
driver2 = Drivers(2, "On Duty")
driver3 = Drivers(3, "Off Duty")

# Initialize truck objects
truck1 = Trucks(101, driver1, package_info_truck1, 0, time_returned_hub1, 0, package_ids1)
truck2 = Trucks(102, driver2, package_info_truck2, 0, time_returned_hub2, 0, package_ids2)
truck3 = Trucks(103, driver3, package_info_truck3, 0, time_returned_hub3, 0, package_ids3)


# This function identifies and returns a list of trucks that are currently available for package delivery.
# It checks the status of each driver and appends the corresponding trucks to the list if the driver is on duty.
def available_trucks():

    trucks_on_duty = []
    if driver1.status == "On Duty":
        trucks_on_duty.append(truck1)
    if driver2.status == "On Duty":
        trucks_on_duty.append(truck2)
    if driver3.status == "On Duty":
        trucks_on_duty.append(truck3)
    return trucks_on_duty


# This function loads packages onto available trucks based on certain criteria,
# It obtains a list of available trucks. It sorts all the package data by zip code.
# It then loads specific packages onto truck2 based on the specified IDs.
# Similarly, specific packages that must be on the same truck are loaded.
# The function then fills other trucks with remaining packages, considering their capacity.
# Once the packages are loaded they are removed from the respective hash table.
def load_trucks(package_ids_must_on_truck2, package_ids_must_be_together, package_delayed):

    list_of_trucks = available_trucks()  # gets list of all available truck

    # All the package data is copied from the package_updates hashtable to the all_packages list
    all_packages = []
    for bucket_list in package_updates.table:
        for package_data in bucket_list:
            all_packages.append(package_data)

    all_packages = sorted(all_packages, key=get_delivery_zipcode)  # data in all_packages list is sorted based on the zip code

    # Iterate through package updates and filter selected packages
    selected_packages = []
    for bucket_list in package_updates.table:
        for pkg_data in bucket_list:
            if pkg_data[0] in package_ids_must_on_truck2:
                selected_packages.append(pkg_data)  # all the packages that must be on truck2 are appended to the selected_packages list

    # Load selected packages onto truck2
    for pkg_data in selected_packages:
        truck2.package_info.append(pkg_data)
        truck2.id_of_package_delivered.append(pkg_data[0])  # this appends the list with a package ID for each package loaded into a truck
        package_updates.remove(pkg_data[0])  # once the truck is loaded with a package, the same package is then removed from the package_updates hash table
        all_packages.remove(pkg_data)  # once the truck is loaded with a package, the same package is then removed from all_packages list

    # Iterate through package updates and filter selected packages
    selected_packages = []
    for bucket_list in package_updates.table:
        for pkg_data in bucket_list:
            if pkg_data[0] in package_ids_must_be_together:
                selected_packages.append(pkg_data)  # all the packages that must be together are appended to the selected_packages list

    # Load selected packages onto truck2
    for pkg_data in selected_packages:
        truck2.package_info.append(pkg_data)
        truck2.id_of_package_delivered.append(pkg_data[0])  # this appends the list with a package ID for each package loaded into a truck
        package_updates.remove(pkg_data[0])  # once the truck is loaded with a package, the same package is then removed from the package_updates hash table
        all_packages.remove(pkg_data)  # once the truck is loaded with a package, the same package is then removed from all_packages list

    # all the remaining packages are loaded onto trucks based on their remaining capacity
    for truck in list_of_trucks:
        remaining_capacity = 16 - len(truck.package_info)  # remaining capacity calculation

        # Iterates through all the remaining packages in all_packages list
        for package_data in all_packages[:]:
            if remaining_capacity > 0:  # ensures that truck's capacity is not full
                # This if statement ensures that the packages that are delayed are not loaded in trip 1
                if (package_data[0] not in package_delayed and truck.miles_travelled == 0) or (truck.miles_travelled != 0):
                    truck.package_info.append(package_data)
                    truck.id_of_package_delivered.append(package_data[0])  # this appends the list with a package ID for each package loaded into a truck
                    package_updates.remove(package_data[0])  # once the truck is loaded with a package, the same package is then removed from the package_updates hash table
                    all_packages.remove(package_data)  # once the truck is loaded with a package, the same package is then removed from all_packages list
                    remaining_capacity -= 1

    return list_of_trucks


package_container = PackageDataHashTable()  # initializes the instance of hash table
package_updates = PackageUpdaterHashTable()  # initializes the instance of hash table

load_package_data('package_file.csv')  # this function takes CSV file as input and populates the package data hash table
