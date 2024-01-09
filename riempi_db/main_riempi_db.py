import os
import json
import mysql.connector
from riempi_db.riempi_db import (
    update_itemLedgerEntries,
    update_capacityledgerentries,
    update_productionorders,
    update_machinecenters,
    update_items,
    update_prodorderroutinglines
)

# Path to the directory containing JSON files
json_folder_path = "G:\Project_Business_Central\BI_Project\json"

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'laboratorio'
}

# Establish connection to MySQL database
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print('Connected to MySQL database')
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")
    exit(1)

# Mapping file names to functions
file_functions = {
    'Item Ledger Entry': update_itemLedgerEntries,
    'Capacity Ledger Entry': update_capacityledgerentries,
    'Production Order': update_productionorders,
    'Machine Center': update_machinecenters,
    'Item': update_items,
    'Prod. Order Routing Line': update_prodorderroutinglines
}

# List all files in the directory
files = os.listdir(json_folder_path)

# Iterate through each file
for file in files:
    if file.endswith(".json"):  # Check if it's a JSON file
        with open(os.path.join(json_folder_path, file), 'r') as f:
            data = json.load(f)

            # Get file name without extension
            file_name = os.path.splitext(file)[0]

            # Call functions based on the file name using the dictionary mapping
            if file_name in file_functions:
                file_functions[file_name](connection, data)  # Pass the connection object to the function

            # Handle cases for unknown file names
            else:
                print(f"No function defined for {file}")

# Close the database connection
if connection.is_connected():
    connection.close()
    print('MySQL connection closed')
