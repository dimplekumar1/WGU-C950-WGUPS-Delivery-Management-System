import csv
from models import *


# This class initializes a hash table to store distance data
# HashTable class using chaining.
class DistanceDataHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=27):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for k in range(initial_capacity):
            self.table.append([])

    # Inserts and update a new item into the hash table.
    def insert(self, distance_id, distance_data):
        # get the bucket list where this item will go.
        bucket = hash(distance_id) % len(self.table)
        bucket_list = self.table[bucket]

        # Insert the data into the bucket
        self.table[bucket].append(distance_data)
        return True

    # This function employs a hash table of distance data to generate a sorted list of nearby delivery locations.
    # This is the key function used in package_delivery function.
    # It searches through the hash table for a given address, extracts distances, filters non-zero values, and sort them.
    # Utilizing an index tracking set, the function retrieves corresponding addresses for these distances.
    # The returned list is a list of sorted delivery addresses in proximity to the specified address.
    def nearest_distances_sorted(self, distance_address):
        sorted_addresses = []  # list to store address in a sorted manner
        sorted_indexes = []  # list to store distance indices in a sorted manner
        non_zero_distances = []  # list to store non-zero distances
        d_data = 0

        # searches for all addresses in the distance_table CSV file until a match is found with the specified address.
        # if a match is found, assigns d_data with the distance row from the CSV file for the matching address
        for bucket_list in self.table:
            for distance_data in bucket_list:
                if distance_data.d_address == distance_address:
                    d_data = distance_data.d_distance

        # It retrieves relevant distance data from the specified address to all other address, appends these distances to a list, and finally, sorts the list in ascending order.
        for num in d_data:
            if num > 0.0:
                non_zero_distances.append(num)
        sorted_distances = sorted(non_zero_distances)

        # This gets the indices of all the distances stored in the sorted_distances list. The stores them in sorted_indexes list
        # These indices will later help determine the distance ID to retrieve the address.
        added_indexes = set()  # To track added indexes
        for target_distance in sorted_distances:
            for index, value in enumerate(d_data):
                if value == target_distance and index not in added_indexes:
                    sorted_indexes.append((index + 2))
                    added_indexes.add(index)

        # This uses search_nearest_delivery_location function. Passes distance ID and gets an address.
        # Addresses are stored in the sorted addresses list.
        for item in sorted_indexes:
            sorted_addresses.append(distanceData.search_nearest_delivery_location(item))

        return sorted_addresses

    # This function retrieves the delivery address linked to a specified distance ID.
    # It iterates through the hash table buckets and their lists to find a matching distance ID.
    def search_nearest_delivery_location(self, distance_id):
        # get the bucket list
        bucket = hash(distance_id) % len(self.table)
        bucket_list = self.table[bucket]

        for distance_data in bucket_list:
            if distance_data.d_id == distance_id:
                return distance_data.d_address

    # This function takes an address as an input and returns associated distance ID.
    # It iterates through the hash table buckets and their lists to find a matching address.
    def distance_id(self, distance_address):
        for bucket_list in self.table:
            for distance_data in bucket_list:
                if distance_data.d_address == distance_address:
                    return distance_data.d_id


# This function is used for processing distance data from a CSV file and populating into a hash table.
# The function iterates through each row and extracts data. Distances are converted from strings to floats.
def load_distance_data(distance_table):
    with open(distance_table) as distance_table:
        distance_data = csv.reader(distance_table, delimiter=',')
        next(distance_data)  # skip header
        for distance in distance_data:
            distance_id = int(distance[0])
            distance_address = distance[1]
            distance_zipcode = distance[2]
            distance_distance = []
            for num_str in distance[3:]:
                num = float(num_str)  # Convert the string to a float
                distance_distance.append(num)
                if num is None:
                    break

            # distance object
            distance_info = DistanceInfo(distance_id, distance_address, distance_zipcode, distance_distance)

            # insert it into the hash table
            distanceData.insert(distance_id, distance_info)


# This function reads data from a CSV file and arranges it into a structures list.
# For each row, distances are extracted and converted into floats.
def load_mileage(mileage_file):
    # Create a list to store mileage data
    mileage_data = []

    # Load the CSV file and populate the mileage_data list
    with open(mileage_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        next(csv_reader)  # Skip the row with address information
        for row in csv_reader:
            distances = []
            for distance in row[1:]:
                distances.append(float(distance))
            mileage_data.append(distances)
    return mileage_data


# This function calculates and returns the distance between two specified locations using the mileage data matrix
# It ensures the validity of provided indices, then retrieves the distance value from the matrix and returns as the distance between the specified locations.
# If the provided indices are out of range, the function returns None
def get_distance_between_two_locations(mileage_data, location_a, location_b):
    if 0 <= location_a < len(mileage_data) and 0 <= location_b < len(mileage_data[location_a]):  # check if the provided indices are valid
        intersection = mileage_data[location_a][location_b]  # gets the distance between provided locations
        return intersection
    else:
        return None


distanceData = DistanceDataHashTable()  # initializes the instance of hash table

load_distance_data('distance_table.csv')  # this function takes CSV file as input and populates the distance data hash table
