#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import random
import string
import pymysql

class Vehicle:
    def __init__(self, vehicle_number, vehicle_type, contact_number, ticket_number, entry_time, exit_time):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.contact_number = contact_number
        self.ticket_number = ticket_number
        self.entry_time = entry_time
        self.exit_time = exit_time
    
    def get_duration(self):
        return self.exit_time - self.entry_time
    
    def get_cost(self):
        duration = self.get_duration()
        total_hours = duration.total_seconds() / 3600
        total_cost = round(total_hours * 10, 2)
        return total_cost
    
    def print_receipt(self):
        total_cost = self.get_cost()
        
        print("--------------- Receipt ---------------")
        print(f"Vehicle Number: {self.vehicle_number}")
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Parking Ticket Number: {self.ticket_number}")
        print(f"Entry Time: {self.entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Exit Time: {self.exit_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Duration: {self.get_duration()}")
        print(f"Total Cost: {total_cost} USD")
        print("---------------------------------------")

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Royalassembly@1',
                             database='parkinglots_db')
cursor = connection.cursor()

# Get user input for vehicle details
vehicle_number = input("Enter vehicle number: ")

# Get user input for vehicle type
print("Select vehicle type:")
print("1. Bike")
print("2. Car")
print("3. Truck")
print("4. Physically disabled")
vehicle_type_choice = input("Enter choice (1-4): ")
vehicle_type_map = {"1": "Bike", "2": "Car", "3": "Truck", "4": "Physically disabled"}
vehicle_type = vehicle_type_map.get(vehicle_type_choice)

contact_number = input("Enter user contact number: ")

# Generate random ticket number
ticket_chars = string.ascii_uppercase + string.digits
ticket_number = ''.join(random.choice(ticket_chars) for _ in range(8))

entry_time_str = input("Enter entry time in YYYY-MM-DD HH:MM:SS format: ")
entry_time = datetime.datetime.strptime(entry_time_str, '%Y-%m-%d %H:%M:%S')
exit_time_str = input("Enter exit time in YYYY-MM-DD HH:MM:SS format: ")
exit_time = datetime.datetime.strptime(exit_time_str, '%Y-%m-%d %H:%M:%S')

# Create Vehicle object and print receipt
vehicle = Vehicle(vehicle_number, vehicle_type, contact_number, ticket_number, entry_time, exit_time)
vehicle.print_receipt()

# Insert parking record into the database
query = f"INSERT INTO parking_records (vehicle_number, vehicle_type, contact_number, ticket_number, entry_time, exit_time) VALUES ('{vehicle_number}', '{vehicle_type}', '{contact_number}', '{ticket_number}', '{entry_time}', '{exit_time}')"
cursor.execute(query)
connection.commit()

# Close the database connection
connection.close()


# In[ ]:




