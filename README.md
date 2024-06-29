# WGUPS Delivery Management System

# **WGUPS Delivery Management System in Python**

## **Project Description:**

This project aims to efficiently manage the delivery of 40 packages for the Western Governors Parcel Service (WGUPS) in Salt Lake City, Utah. It involves applying algorithms and data structures to ensure on-time deliveries while keeping the total travel distance under 140 miles.

## **Key Features:**

1. **Algorithm Identification:** The program employs Nearest Neighbor algorithm to optimize package delivery routes. This algorithm selects the closest available package at each step, minimizing travel distance and time.

2. **Development Environment:** The project was developed using PyCharm 2023.1.2 (Community Edition) with Python 3.11.

3. **Data Structures and Assumptions:** The project employs hash tables for efficient data storage and retrieval. Key assumptions include:
    - Each truck can carry a maximum of 16 packages.
    - Trucks travel at 18 mph with infinite gas.
    - Three trucks and two drivers are available.
    - Drivers start at 8:00 a.m. with loaded trucks.
    - Delivery and loading times are instantaneous.
    - Specific package constraints are accounted for.

4. **Functionality for Data Manipulation:** The implemented program provides functions to load trucks, find nearest delivery locations, deliver packages, and check delivery status at specified times. These functions ensure efficient package handling and delivery route optimization.

5. **Scalability and Adaptability:** The system is designed to be scalable and adaptable, handling package growth and different constraints with ease. It can be customized for more trucks, drivers, and varied delivery criteria.

6. **User Interface:** The program provides an interactive user interface for viewing package status and total mileage traveled by trucks.

## **How to Use:**

The repository contains the complete Python source code for the project. To utilize it, follow these steps:

1. Clone the repository to your local machine using the command `git clone <repository-url>`.
2. Open the project in PyCharm or your preferred Python IDE.
3. Ensure you have Python 3.11 installed on your system.
4. Run the main script to execute the package delivery management system.
5. Follow the on-screen prompts to interact with the system, check package status, and view total mileage.

## **Strengths of the Algorithm:**

The Nearest Neighbor algorithm offers several strengths:

1. **Efficient Route Optimization:** It optimizes routes by selecting the closest package, minimizing travel distance and time.
2. **Responsiveness to Delivery Constraints:** The algorithm adapts to various constraints, ensuring efficient deliveries.

## **Alternative Algorithms:**

While Nearest Neighbor is effective, alternative algorithms to consider are Dijkstra's Algorithm or Genetic Algorithm.

*For detailed code implementation, please refer to the source code files in the project repository.*
