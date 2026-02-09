import csv
import rules
import plots
import statistics

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

#Main program

"""
    Main functions
    
   x 1. Read csv file
   x 2. Validate Data
   x 2.1 Check if csv is empty
    3. Calculate Statistics
    3.1 Calculate mean
    3.2 Calculate median
    3.3 Calculate range
    3.4 Calculate standard deviation
    4. Error Detection
    4.1 Check for outliers
    4.2 Check for missing values
    5. Output Results
    5.1 Print statistics
    5.2 Print error detections
    6. Create and Save Plot
    6.1 Create plot of the data
    6.2 Save plot as image file
    """

"""
1. Read csv file
"""

def read_csv():
    username = os.getenv("USERNAME", "default_user")
    data_path = f"/Users/{username}/Documents/Programming/MINT/data/data.csv"
    with open(data_path) as file:
        reader = csv.reader(file)
        data = list(reader)
        for row in data:
            print(row)
        return data

"""
2. Validate Data
2.1 Check if csv is empty
"""
def validate_data(data):
    # Validate the data (csv empty?)
    if not data:
        print("Error: The CSV file is empty.")
        return False
    return True

"""
3. Calculate Statistics
3.1 Calculate mean
3.2 Calculate median
3.3 Calculate range
3.4 Calculate standard deviation
"""
def calculate_statistics(reader): 
    pass


data = read_csv()
# If data is valid, calculate statistics
if validate_data(data):
    calculate_statistics(data)