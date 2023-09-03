# WGUPS Delivery Management System

## Introduction

In this project, the goal is to apply algorithms and data structures practically by addressing a real-world programming challenge. The task involves using an algorithm to effectively guide delivery trucks for the Western Governors Parcel Service (WGUPS), ensuring adherence to delivery criteria while maintaining a total travel distance within 140 miles. The project requires the creation of a Python program to manage delivery of 40 packages, some with specific conditions, using provided distance information.

## Algorithm Identification

My program uses Nearest Neighbor algorithm for optimizing package delivery routes. This approach involves selecting the closest available package at each step of the route, effectively minimizing travel distance and time.

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

## C950 WGUPS Algorithm Overview

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
           - DELIVER the package and UPDATE status
           - UPDATE mileage and time
           - REMOVE package from truck
           - SET current location to the delivery address
           - FOR other packages with the same delivery address
             - DELIVER the package and UPDATE status
             - UPDATE mileage and time
             - REMOVE package from truck
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

## Development Environment

- IDE: PyCharm 2023.1.2 (Community Edition)
- Python Version: Python 3.11
- Operating System: macOS Ventura (Version 13.2.1)
- Processor: 2.3 GHz Dual-Core Intel Core i5
- Graphics: Intel Iris Plus Graphics 640 (1536 MB)
- Memory: 8GB RAM

## Scalability and Adaptability

The program can be enhanced for scalability and adaptability:

- Scalability:
  - The program can efficiently handle a growing number of packages due to its use of hash tables for package and distance data storage.
  - Increasing the number of drivers and trucks may require minor modifications to the code.

- Adaptability:
  - The program can adapt to different constraints, such as changes in package priorities or address updates, without significant code changes.
  - It can be modified to accommodate more trucks and drivers, as well as different delivery criteria, with minimal adjustments.

## Software Efficiency and Maintainability

The code is designed for efficiency and maintainability:

- Efficient:
  - The use of hash tables allows for quick data retrieval and updates.
  - Code is organized into functions, promoting reusability and readability.
  - Complex tasks are broken down into smaller functions for easier maintenance.

- Maintainable:
  - The program is well-structured and follows PEP 8 coding conventions.
  - Functions are named descriptively, making the code self-documenting.
  - Comments provide explanations for complex logic and data structures.
  - Error handling is implemented to ensure the program handles unexpected input gracefully.

## Self-Adjusting Data Structures

The program utilizes hash tables as self-adjusting data structures:

- Hash Tables:
  - Hash tables are used for storing package and distance data.
  - They efficiently store and retrieve data based on keys (package IDs and distance IDs).
  - Hash table implementations include methods for inserting, retrieving, updating, and removing data.

## Hash Table Insertion Function

The insertion function for hash tables takes package components (for package data) or distance components (for distance data) as input and inserts them into the respective hash table. The package ID or distance ID serves as the key for insertion.

## Hash Table Look-Up Function

The look-up function for hash tables takes package components (for package data) or distance components (for distance data) as input and returns the corresponding data elements based on the provided package ID or distance ID. This function efficiently retrieves data from the hash table using the key.

## User Interface

The program provides an interactive user interface for viewing the status and information of packages at any given time. It also allows users to check the total mileage traveled by all trucks.

## Code Execution Screenshots

Screenshots demonstrating the successful execution of the code without runtime errors or warnings, along with the display of the total mileage traveled by all trucks, are included in the project documentation.

## Justification of Core Algorithm

### Strengths of the Algorithm

The Nearest Neighbor algorithm used in this project offers several strengths:

1. Efficient Route Optimization: The algorithm optimizes delivery routes by selecting the closest available package at each step, effectively minimizing travel distance and time.

2. Responsiveness to Delivery Constraints: The algorithm adapts to various constraints, such as packages that must be delivered together or address updates, ensuring efficient deliveries.

### Algorithm Verification

The Nearest Neighbor algorithm meets all the project requirements, delivering all packages on time and within the mileage limit.

### Alternative Algorithms

Two alternative algorithms to consider for this project are:

1. Dijkstra's Algorithm: This algorithm is suitable for finding the shortest path in a graph. However, it may be computationally expensive for large datasets and may not prioritize delivery constraints.

2. Genetic Algorithm: Genetic algorithms are evolutionary optimization techniques. While they can provide efficient solutions, they may require more complex implementation and tuning compared to the Nearest Neighbor algorithm.

## What Would Be Done Differently

If this project were to be redone, several improvements and modifications could be considered:

- Optimization of Time Complexity: The code could be optimized to reduce nested loops and improve overall time complexity.

- Enhanced Code Modularity: The code could be further divided into smaller, reusable modules to improve maintainability.

- Removal of Restrictions: The code could be made more flexible by removing restrictions on the number of trucks and drivers, allowing for greater adaptability.

## Justification of Data Structure

### Verification of Data Structure

The hash table-based data structure employed in this project effectively meets all project requirements, providing efficient data retrieval and updates based on package and distance IDs. However, an increase in the number of packages may impact lookup times in worst-case scenarios.

### Efficiency

- Hash tables provide an average-case time complexity of O(1) for insertion, deletion, and lookup operations.

- In worst-case scenarios with hash table collisions, time complexity can reach O(n), but such scenarios are unlikely to significantly impact performance in this context.

### Overhead

- The space complexity of the hash tables used in this project is O(n), directly influenced by the number of packages being managed.

### Implications

1. Increase in Number of Trucks: Adding more trucks has a linear impact on space complexity (O(n)) for the list of trucks.

2. Increase in Number of Cities: Expanding the delivery area has minimal impact on lookup times, as the space complexity for the distance hash table remains O(n).

---

*For detailed code implementation, please refer to the source code files in the project repository.*

