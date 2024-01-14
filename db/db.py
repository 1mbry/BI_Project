import mysql.connector

# Metodo per stabilire la connessione al data warehouse MySQL
def establish_mysql_connection(host, user, password):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        if connection.is_connected():
            print('Connessione al data warehouse MySQL')
        return connection
    except mysql.connector.Error as error:
        print("Error:", error)
        return None

# Metodo per stabilire la connessione al database "laboratorio"
def establish_db_connection(host, user, password, database_name):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )
        if connection.is_connected():
            print('Connessione al database laboratorio')
        return connection
    except mysql.connector.Error as error:
        print("Error:", error)
        return None

# Metodo che controlla se il database laboratorio esiste
def does_database_exist(conn, database_name):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
        result = cursor.fetchone()
        return result is not None
    except mysql.connector.Error as err:
        print(f"Si è verificato un errore: {err}")
        return False
    finally:
        cursor.close()

# Metodo che mi crea il database laboratorio
def create_database(conn, database_name):
    try:
        cursor = conn.cursor()
        query = f"CREATE DATABASE {database_name}"
        cursor.execute(query)

        print(f"Database '{database_name}' creato con successo.")

    except mysql.connector.Error as err:
        print(f"Errore: {err}")

    finally:
        cursor.close()

# Metodo che controlla se le tabelle esistono nel database laboratorio
def do_tables_exist(conn):
    try:
        cursor = conn.cursor()
        tables = [
            'itemledgerentries',
            'capacityledgerentries',
            'productionorders',
            'machinecenters',
            'items',
            'prodorderroutinglines'
        ]

        for table in tables:
            # Controllo che le tabelle esistano
            cursor.execute(f"SHOW TABLES LIKE '{table}'")
            result = cursor.fetchone()

            if not result:
                # Se non esistono ritorno False
                return False

        # Se esistono ritorno True
        return True

    except mysql.connector.Error as err:
        print(f"Error checking table existence: {err}")
        return False

    finally:
        cursor.close()

# Metodo che mi crea le tabelle nel database laboratorio
def create_tables(conn):
    try:
        cursor = conn.cursor()

        tables = """
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

        cursor.execute(tables)
        
        print("Tabelle create con successo")

        # Aggiorna la connessione dopo aver creato le tabelle
        conn.close()
        conn = establish_db_connection('localhost', 'root', '', 'laboratorio')

    except mysql.connector.Error as err:
        print(f"Errore durante la connessione al database: {err}")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

    finally:
        cursor.close()

    return conn