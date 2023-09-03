
# This class defines a structure to represent delivery packages and their relevant information.
class Package:
    def __init__(self, p_id, p_address, p_deadline, p_city, p_zipcode, p_weight, p_status):
        self.p_id = p_id
        self.p_address = p_address
        self.p_deadline = p_deadline
        self.p_city = p_city
        self.p_zipcode = p_zipcode
        self.p_weight = p_weight
        self.p_status = p_status

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return f"{self.p_id}, {self.p_address}, {self.p_deadline}, {self.p_city},  {self.p_zipcode},{self.p_weight}, " \
               f"{self.p_status}"


# This class defines a structure to represent distance data and its relevant information.
class DistanceInfo:
    def __init__(self, d_id, d_address, d_zipcode, d_distance):
        self.d_id = d_id
        self.d_address = d_address
        self.d_zipcode = d_zipcode
        self.d_distance = d_distance

    def __str__(self):  # overwrite print(Distance) otherwise it will print object reference
        return f"{self.d_id}, {self.d_address}, {self.d_zipcode}, {self.d_distance}"


# This class defines a structure to represent delivery trucks and their relevant information.
class Trucks:
    def __init__(self, truck_id, driver, pac_info, miles_travelled, last_time_returned_hub, num_package_delivered, id_of_package_delivered):
        self.truck_id = truck_id
        self.driver = driver
        self.package_info = pac_info
        self.miles_travelled = miles_travelled
        self.last_time_returned_hub = last_time_returned_hub
        self.num_package_delivered = num_package_delivered
        self.id_of_package_delivered = id_of_package_delivered

    def __str__(self):  # overwrite print(Trucks) otherwise it will print object reference
        return f"{self.truck_id} ,{self.driver}, {self.package_info}, {self.miles_travelled}, {self.last_time_returned_hub}, {self.num_package_delivered}, {self.id_of_package_delivered}"


# This class defines a structure to represent delivery drivers and their relevant information.
class Drivers:
    def __init__(self, driver_id, status):
        self.driver_id = driver_id
        self.status = status

    def __str__(self):  # overwrite print(Drivers) otherwise it will print object reference
        return f"{self.driver_id}, {self.status}"
