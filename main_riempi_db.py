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
json_folder_path = "riempi_db\json"

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
    
    try:
        # If database does not exist, create it
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password']
        )
        cursor = connection.cursor()

        # Define your database creation query here
        create_db_query = "CREATE DATABASE IF NOT EXISTS laboratorio;"
        cursor.execute(create_db_query)
        print("Database created successfully")

        # Now, select the database 'laboratorio'
        cursor.execute("USE laboratorio;")

        # Define your table creation queries here
        create_tables_query = """
            CREATE TABLE item_ledger ( id INT AUTO_INCREMENT PRIMARY KEY, entry_no INT, entry_type VARCHAR(255), item_no VARCHAR(255), document_no VARCHAR(255), quantity FLOAT, posting_date DATE, cost_amount_actual FLOAT );

            CREATE TABLE capacity_ledger ( id INT AUTO_INCREMENT PRIMARY KEY, entry_no INT, order_type VARCHAR(255), type VARCHAR(255), no VARCHAR(255), document_no VARCHAR(255), item_no VARCHAR(255), routing_no VARCHAR(255), quantity FLOAT, output_quantity FLOAT, scrap_quantity FLOAT, direct_cost FLOAT, overhead_cost FLOAT, run_time FLOAT, setup_time FLOAT, starting_time DATETIME, ending_time DATETIME, stop_time DATETIME, posting_date DATE );

            CREATE TABLE production_orders ( id INT AUTO_INCREMENT PRIMARY KEY, no VARCHAR(255), status VARCHAR(255), description VARCHAR(255), creation_date DATE, quantity FLOAT, source_no VARCHAR(255), assigned_worker VARCHAR(255), due_date DATE, starting_date DATE, ending_date DATE, starting_time DATETIME, ending_time DATETIME );

            CREATE TABLE machine_centers ( id INT AUTO_INCREMENT PRIMARY KEY, no VARCHAR(255), name VARCHAR(255) );

            CREATE TABLE items ( id INT AUTO_INCREMENT PRIMARY KEY, no VARCHAR(255), description VARCHAR(255), routing_no VARCHAR(255), production_bom_no VARCHAR(255) );

            CREATE TABLE prodorderroutinglines ( id INT AUTO_INCREMENT PRIMARY KEY, operation_no VARCHAR(255), type VARCHAR(255), no VARCHAR(255), status VARCHAR(255), prodorder_no VARCHAR(255), description VARCHAR(255), routing_no VARCHAR(255), work_center_no VARCHAR(255), starting_date DATE, starting_time DATETIME, direct_unit_cost FLOAT, expected_operation_cost_amt FLOAT, unit_cost_per FLOAT, setup_time FLOAT, run_time FLOAT );
        """

        cursor.execute(create_tables_query)
        print("Tables created successfully")
        print ("Restart the script to fill the tables")
        exit(1)

    except mysql.connector.Error as create_db_error:
        print(f"Error creating database or tables: {create_db_error}")
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
