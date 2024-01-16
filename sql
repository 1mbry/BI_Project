"""
            CREATE TABLE IF NOT EXISTS itemledgerentries (
                id INT AUTO_INCREMENT PRIMARY KEY,
                entry_no INT,
                entry_type VARCHAR(255),
                item_no VARCHAR(255),
                order_type VARCHAR(255),
                document_no VARCHAR(255),
                quantity DECIMAL(10,2),
                posting_date DATE,
                cost_amount_actual DECIMAL(10,2),
                UNIQUE KEY unique_entry_item (entry_no, entry_type, item_no)
            ); 
            
            CREATE TABLE IF NOT EXISTS capacityledgerentries (
                id INT AUTO_INCREMENT PRIMARY KEY,
                entry_no INT,
                order_type VARCHAR(255),
                type VARCHAR(255),
                no VARCHAR(255),
                document_no VARCHAR(255),
                item_no VARCHAR(255),
                routing_no VARCHAR(255),
                quantity DECIMAL(10,2),
                output_quantity DECIMAL(10,2),
                scrap_quantity DECIMAL(10,2),
                direct_cost DECIMAL(10,2),
                overhead_cost DECIMAL(10,2),
                run_time DECIMAL(10,2),
                setup_time DECIMAL(10,2),
                starting_time TIME,
                ending_time TIME,
                stop_time DECIMAL(10,2),
                posting_date DATE,
                UNIQUE KEY unique_entry (entry_no, order_type, type, item_no)
            );

            CREATE TABLE IF NOT EXISTS productionorders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                no VARCHAR(255),
                status VARCHAR(255),
                description VARCHAR(255),
                creation_date DATE,
                quantity DECIMAL(10,2),
                source_no VARCHAR(255),
                assigned_worker VARCHAR(255),
                due_date DATE,
                starting_date DATE,
                ending_date DATE,
                starting_time TIME,
                ending_time TIME,
                UNIQUE KEY unique_order (no)
            );

            CREATE TABLE IF NOT EXISTS machinecenters (
                id INT AUTO_INCREMENT PRIMARY KEY,
                no VARCHAR(255),
                name VARCHAR(255),
                UNIQUE KEY unique_center (no)
            );

            CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                no VARCHAR(255),
                description VARCHAR(255),
                routing_no VARCHAR(255),
                production_bom_no VARCHAR(255),
                inventory DECIMAL(10,2),
                UNIQUE KEY unique_item (no)
            );


            CREATE TABLE IF NOT EXISTS prodorderroutinglines (
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
                starting_time TIME,
                direct_unit_cost DECIMAL(10,2),
                expected_operation_cost_amt DECIMAL(10,2),
                unit_cost_per DECIMAL(10,2),
                setup_time DECIMAL(10,2),
                run_time DECIMAL(10,2),
                UNIQUE KEY unique_routing_line (no)
            );
            """
