# BI_Project
I am working on a BI project that involves utilizing Metabase alongside a Python script, integrating Business Central On-Premise and Power Apps.
The server setup includes SQL Server, while for the data warehouse, I am utilizing MySQL.


## codice sql
CREATE TABLE item_ledger (
    id INT AUTO_INCREMENT PRIMARY KEY,
    entry_no INT,
    entry_type VARCHAR(255),
    item_no VARCHAR(255),
    document_no VARCHAR(255),
    quantity FLOAT,
    posting_date DATE,
    cost_amount_actual FLOAT
);

CREATE TABLE capacity_ledger (
    id INT AUTO_INCREMENT PRIMARY KEY,
    entry_no INT,
    order_type VARCHAR(255),
    type VARCHAR(255),
    no VARCHAR(255),
    document_no VARCHAR(255),
    item_no VARCHAR(255),
    routing_no VARCHAR(255),
    quantity FLOAT,
    output_quantity FLOAT,
    scrap_quantity FLOAT,
    direct_cost FLOAT,
    overhead_cost FLOAT,
    run_time FLOAT,
    setup_time FLOAT,
    starting_time DATETIME,
    ending_time DATETIME,
    stop_time DATETIME,
    posting_date DATE
);

-- Create other tables similarly based on your functions
CREATE TABLE production_orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    no VARCHAR(255),
    status VARCHAR(255),
    description VARCHAR(255),
    creation_date DATE,
    quantity FLOAT,
    source_no VARCHAR(255),
    assigned_worker VARCHAR(255),
    due_date DATE,
    starting_date DATE,
    ending_date DATE,
    starting_time DATETIME,
    ending_time DATETIME
);

CREATE TABLE machine_centers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    no VARCHAR(255),
    name VARCHAR(255)
);

CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    no VARCHAR(255),
    description VARCHAR(255),
    routing_no VARCHAR(255),
    production_bom_no VARCHAR(255)
);

CREATE TABLE prodorderroutinglines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    operation_no VARCHAR(255),
    type VARCHAR(255),
    no VARCHAR(255),
    status VARCHAR(255),
    prodorder_no VARCHAR(255),
    description VARCHAR(255),
    routing_no VARCHAR(255),
    work_center_no VARCHAR(255),
    starting_date DATE,
    starting_time DATETIME,
    direct_unit_cost FLOAT,
    expected_operation_cost_amt FLOAT,
    unit_cost_per FLOAT,
    setup_time FLOAT,
    run_time FLOAT
);
