# WGUPS Delivery Management System

## Introduction

This project aims to efficiently manage the delivery of 40 packages for the Western Governors Parcel Service (WGUPS) in Salt Lake City, Utah. It involves applying algorithms and data structures to ensure on-time deliveries while keeping the total travel distance under 140 miles.

## Scenario

WGUPS operates with three trucks, two drivers, and 40 packages, each with specific criteria. The goal is to optimize delivery routes, adhering to constraints like maximum travel distance and specific delivery requirements.

## Algorithm Identification

I use the Nearest Neighbor algorithm to optimize package delivery routes. This algorithm selects the closest available package at each step, minimizing travel distance and time.

## Development Environment

- **IDE:** PyCharm 2023.1.2 (Community Edition)
- **Python Version:** Python 3.11
- **Operating System:** macOS Ventura (Version 13.2.1)
- **Processor:** 2.3 GHz Dual-Core Intel Core i5
- **Graphics:** Intel Iris Plus Graphics 640 (1536 MB)
- **Memory:** 8GB RAM

## Assumptions

Key assumptions for this project:

- Each truck can carry a maximum of 16 packages.
- Trucks travel at 18 mph with infinite gas.
- Three trucks and two drivers are available.
- Drivers start at 8:00 a.m. with loaded trucks.
- Delivery and loading times are instantaneous.
- One special note is associated with a package.
- Distances are equal regardless of direction.
- The day ends when all 40 packages are delivered.

## Logic Comments/Pseudo-code

1. Initialize packages and distances:
   - CREATE a hash table to store package information and its associated methods.
   - CREATE a hash table to store distance information and its associated methods.

2. Load package and distance data:
   - LOAD package details from the CSV file into the package hash table.
   - LOAD distance information from the CSV file into the distance hash table.

3. Create trucks and driver objects:
   - CREATE and initialize three drivers.
   - CREATE and initialize three trucks.

4. Function to provide a list of available trucks:
   - CREATE an empty list to add available trucks.
   - IF Driver 1 is working THEN
     - ADD Truck1 to the list.
   - IF Driver 2 is working THEN
     - ADD Truck2 to the list.
   - IF Driver 3 is working THEN
     - ADD Truck3 to the list.
   - RETURN the list of available trucks.

5. Function to load trucks with packages:
   - GET the list of available trucks.
   - CREATE a new list to add packages.
   - COPY all packages to the new list.
   - SORT the new list of packages based on zip code.
   - LOAD all the packages that must go on truck2.
   - LOAD all the packages that must go together on truck2.
   - LOAD remaining packages among all trucks:
   - FOR each truck in the truck list
     - FOR each package in the new list
       - IF there is space in the truck
         - IF (package is not delayed and truck hasn’t moved) or truck has moved
           - ADD remaining package to the truck
           - REDUCE the remaining space in truck
   - RETURN the list of trucks with packages on them.

6. Function to find nearest delivery location:
   - CREATE an empty list to store addresses.
   - FOR each distance address in the hash table
     - IF the distance address matches the function input address
       - CREATE a new list to store non-zero distances
       - GET distances from input address to all other addresses and store in this list
       - SORT these distances in ascending order
       - FOR each distance in sorted distances list
         - GET corresponding address
         - STORE this address in the list created at the beginning of this function
   - RETURN the list containing sorted addresses.

7. Function to deliver packages:
   - FOR each truck in the list of trucks
     - SET the initial delivery time and location
     - IF truck hasn’t returned to hub before THEN
       - Use initial time
     - ELSE
       - Use last return to hub time
     - WHILE truck has packages
       - FIND the nearest delivery address from current location
       - FOR each package in the truck
         - IF package address matches the nearest delivery address
           - DELIVER all packages with that address and UPDATE status
           - UPDATE mileage and time
           - REMOVE package from truck
           - SET current location to the delivery address
           - STOP searching for packages at this address
         - IF no matching package address
           - PRINT a message
           - UPDATE mileage and time for truck returning to hub after package deliveries
           - RECORD the return to hub time

8. Function to execute package delivery:
   - CREATE a list of packages that must go on Truck2
   - CREATE a list of packages that must go on the same truck
   - CREATE a list of delayed packages
   - CREATE a list for an address update information for a package
   - LOAD trucks for trip 1 with specified packages
   - DELIVER packages for trip 1
   - SET driver of truck 2 to Off Duty
   - LOAD trucks for trip 2 with remaining packages
   - DELIVER remaining packages for trip 2

9. Function to check delivery status at a specified time:
   - FOR each package in the hash table
     - FIND the truck that delivered the package
     - FIND the package delivery time
     - IF delivery time was earlier than or equal to the specified time
       - CONTINUE
     - ELSE
       - IF the truck's latest return time is after specified time and also after the earliest return time
         - UPDATE package status to “At Hub”
       - ELSE
         - UPDATE package status to “En Route”
         - CALCULATE mileage up to the specified time

10. Interactive options for the user:
    - WHILE True
      - Show the menu options and ask what the user wants to do
      - IF user chooses a valid option THEN
        - EXIT the loop
      - IF user chooses to get total mileage THEN
        - DELIVER all packages
        - SHOW status of all packages and total mileage of all trucks finishing all the deliveries
      - IF user chooses to check the status of all packages at the certain time THEN
        - ASK for a valid time input
        - DELIVER all packages
        - SHOW status of packages and mileage at that time
      - IF user chooses to check the status of an individual package at the particular time THEN
        - ASK for a valid package ID input
        - ASK for a valid time input
        - DELIVER all packages
        - SHOW the package status at that time
      - IF user chooses to exit THEN
        - END the program

## Scalability and Adaptability

This system is designed to be scalable and adaptable:

- **Scalability**: The program efficiently handles package growth due to its hash table data storage. Adding more trucks or drivers requires minimal code adjustments.

- **Adaptability**: The system adapts to different constraints, such as package priorities or address updates, with ease. It can be customized for more trucks, drivers, and varied delivery criteria.

## Software Efficiency and Maintainability

The code focuses on efficiency and maintainability:

- **Efficiency**: Hash tables ensure quick data retrieval, and modular code promotes reusability. Complex tasks are divided into smaller functions for easier maintenance.

- **Maintainability**: The code is well-structured, follows naming conventions, and is documented with comments. Error handling ensures graceful handling of unexpected input.

## Self-Adjusting Data Structures

I use hash tables as self-adjusting data structures:

- Hash tables efficiently store and retrieve data based on keys.
- The implementations include methods for data manipulation.

## User Interface

The program provides an interactive user interface for viewing package status and total mileage traveled by trucks.

## Strengths of the Algorithm

The Nearest Neighbor algorithm offers several strengths:

1. **Efficient Route Optimization**: It optimizes routes by selecting the closest package, minimizing travel distance and time.

2. **Responsiveness to Delivery Constraints**: The algorithm adapts to various constraints, ensuring efficient deliveries.

## Alternative Algorithms

While Nearest Neighbor is effective, alternative algorithms to consider are Dijkstra's Algorithm or Genetic Algorithm.

## What Could Be Done Differently

In a future iteration, the following improvements could be considered:

- **Optimization of Time Complexity**: Optimize code to reduce nested loops and improve time complexity.

- **Enhanced Code Modularity**: Further divide the code into smaller, reusable modules.

- **Removal of Restrictions**: Make the code more flexible by removing restrictions on the number of trucks and drivers.

---

*For detailed code implementation, please refer to the source code files in the project repository.*

