import mysql.connector

def update_itemLedgerEntries(conn, result):
    try:
            cursor = conn.cursor()

            for data in result['value']:
                # Rimuovere le colonne indesiderate dal dizionario data
                excluded_columns = ["@odata.etag", "SystemId"]
                data = {key: value for key, value in data.items() if key not in excluded_columns}
                
                cursor.execute("""
                INSERT INTO item_ledger 
                (entry_no, item_no, posting_date, entry_type, source_no, document_no, description, quantity,
                sales_amount_actual, cost_amount_actual, last_modified_date_time) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
                ON DUPLICATE KEY UPDATE 
                item_no = VALUES(item_no), posting_date = VALUES(posting_date), entry_type = VALUES(entry_type), 
                source_no = VALUES(source_no), document_no = VALUES(document_no), description = VALUES(description), 
                quantity = VALUES(quantity), sales_amount_actual = VALUES(sales_amount_actual),
                cost_amount_actual = VALUES(cost_amount_actual), last_modified_date_time = VALUES(last_modified_date_time)
            """,
            (data['entryNumber'], data['itemNumber'], data['postingDate'], data['entryType'],
            data['sourceNumber'], data['documentNumber'], data['description'], data['quantity'],
            data['salesAmountActual'], data['costAmountActual'], data['lastModifiedDateTime']))

            # Commit delle modifiche
            conn.commit()

    except mysql.connector.Error as err:
        print(f"Errore durante la connessione al database: {err}")

    except Exception as e:
        print(f"Si è verificato un errore: {e}")

    finally:
        # Chiusura della connessione al database
        cursor.close()


def update_capacityledgerentries(conn, result):
    try:
        cursor = conn.cursor()

        for data in result['value']:
            excluded_columns = ["@odata.etag"]
            data = {key: value for key, value in data.items() if key not in excluded_columns}

            cursor.execute("""
                INSERT INTO capacity_ledger 
                (entry_no, order_type, type, no, document_no, item_no, routing_no, quantity, output_quantity,
                scrap_quantity, direct_cost, overhead_cost, run_time, setup_time, starting_time, ending_time,
                stop_time, posting_date) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
                ON DUPLICATE KEY UPDATE 
                order_type = VALUES(order_type), type = VALUES(type), no = VALUES(no),
                document_no = VALUES(document_no), item_no = VALUES(item_no),
                routing_no = VALUES(routing_no), quantity = VALUES(quantity),
                output_quantity = VALUES(output_quantity), scrap_quantity = VALUES(scrap_quantity),
                direct_cost = VALUES(direct_cost), overhead_cost = VALUES(overhead_cost),
                run_time = VALUES(run_time), setup_time = VALUES(setup_time),
                starting_time = VALUES(starting_time), ending_time = VALUES(ending_time),
                stop_time = VALUES(stop_time), posting_date = VALUES(posting_date)
            """, (
                data['entry_no'], data['order_type'], data['type'], data['no'], data['document_no'],
                data['item_no'], data['routing_no'], data['quantity'], data['output_quantity'],
                data['scrap_quantity'], data['direct_cost'], data['overhead_cost'], data['run_time'],
                data['setup_time'], data['starting_time'], data['ending_time'], data['stop_time'],
                data['posting_date']
            ))

        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        cursor.close()

def update_productionorders(conn, result):
    try:
        cursor = conn.cursor()

        for data in result['value']:
            excluded_columns = ["@odata.etag"]
            data = {key: value for key, value in data.items() if key not in excluded_columns}

            cursor.execute("""
                INSERT INTO production_orders 
                (no, status, description, creation_date, quantity, source_no, assigned_worker, due_date,
                starting_date, ending_date, starting_time, ending_time) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
                ON DUPLICATE KEY UPDATE 
                status = VALUES(status), description = VALUES(description), creation_date = VALUES(creation_date),
                quantity = VALUES(quantity), source_no = VALUES(source_no), assigned_worker = VALUES(assigned_worker),
                due_date = VALUES(due_date), starting_date = VALUES(starting_date),
                ending_date = VALUES(ending_date), starting_time = VALUES(starting_time),
                ending_time = VALUES(ending_time)
            """, (
                data['no'], data['status'], data['description'], data['creation_date'],
                data['quantity'], data['source_no'], data['assigned_worker'], data['due_date'],
                data['starting_date'], data['ending_date'], data['starting_time'], data['ending_time']
            ))

        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        cursor.close()


def update_machinecenters(conn, result):
    try:
        cursor = conn.cursor()

        for data in result['value']:
            excluded_columns = ["@odata.etag"]
            data = {key: value for key, value in data.items() if key not in excluded_columns}

            cursor.execute("""
                INSERT INTO machine_centers (no, name)
                VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE 
                name = VALUES(name)
            """, (
                data['no'], data['name']
            ))

        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        cursor.close()


def update_items(conn, result):
    try:
        cursor = conn.cursor()

        for data in result['value']:
            excluded_columns = ["@odata.etag", "SystemId"]
            data = {key: value for key, value in data.items() if key not in excluded_columns}

            cursor.execute("""
                INSERT INTO items (number, displayName, type, itemCategoryId, itemCategoryCode, blocked,
                gtin, inventory, unitPrice, priceIncludesTax, unitCost, taxGroupId, taxGroupCode,
                baseUnitOfMeasureId, baseUnitOfMeasureCode, generalProductPostingGroupId,
                generalProductPostingGroupCode, inventoryPostingGroupId, inventoryPostingGroupCode,
                lastModifiedDateTime)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                number = VALUES(number), displayName = VALUES(displayName), type = VALUES(type),
                itemCategoryId = VALUES(itemCategoryId), itemCategoryCode = VALUES(itemCategoryCode),
                blocked = VALUES(blocked), gtin = VALUES(gtin), inventory = VALUES(inventory),
                unitPrice = VALUES(unitPrice), priceIncludesTax = VALUES(priceIncludesTax),
                unitCost = VALUES(unitCost), taxGroupId = VALUES(taxGroupId), taxGroupCode = VALUES(taxGroupCode),
                baseUnitOfMeasureId = VALUES(baseUnitOfMeasureId), baseUnitOfMeasureCode = VALUES(baseUnitOfMeasureCode),
                generalProductPostingGroupId = VALUES(generalProductPostingGroupId),
                generalProductPostingGroupCode = VALUES(generalProductPostingGroupCode),
                inventoryPostingGroupId = VALUES(inventoryPostingGroupId),
                inventoryPostingGroupCode = VALUES(inventoryPostingGroupCode),
                lastModifiedDateTime = VALUES(lastModifiedDateTime)
            """, (
                data['number'], data['displayName'], data['type'], data['itemCategoryId'],
                data['itemCategoryCode'], data['blocked'], data['gtin'], data['inventory'], data['unitPrice'],
                data['priceIncludesTax'], data['unitCost'], data['taxGroupId'], data['taxGroupCode'],
                data['baseUnitOfMeasureId'], data['baseUnitOfMeasureCode'], data['generalProductPostingGroupId'],
                data['generalProductPostingGroupCode'], data['inventoryPostingGroupId'],
                data['inventoryPostingGroupCode'], data['lastModifiedDateTime']
            ))

        conn.commit()

    except mysql.connector.Error as err:
        print(f"Errore durante la connessione al database: {err}")

    except Exception as e:
        print(f"Si è verificato un errore: {e}")

    finally:
        # Chiusura della connessione al database
        cursor.close()

def update_prodorderroutinglines(conn, result):
    try:
        cursor = conn.cursor()

        for data in result['value']:
            excluded_columns = ["@odata.etag"]
            data = {key.lower(): value for key, value in data.items() if key.lower() not in excluded_columns}

            cursor.execute("""
                INSERT INTO prodorderroutinglines (operation_no, type, no, status, prodorder_no, description,
                routing_no, work_center_no, starting_date, starting_time, direct_unit_cost, 
                expected_operation_cost_amt, unit_cost_per, setup_time, run_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE 
                type = VALUES(type), status = VALUES(status), prodorder_no = VALUES(prodorder_no), 
                description = VALUES(description), routing_no = VALUES(routing_no), work_center_no = VALUES(work_center_no),
                starting_date = VALUES(starting_date), starting_time = VALUES(starting_time), 
                direct_unit_cost = VALUES(direct_unit_cost), expected_operation_cost_amt = VALUES(expected_operation_cost_amt),
                unit_cost_per = VALUES(unit_cost_per), setup_time = VALUES(setup_time), run_time = VALUES(run_time)
            """, (
                data['operation_no'], data['type'], data['no'], data['status'], data['prodorder_no'],
                data['description'], data['routing_no'], data['work_center_no'], data['starting_date'],
                data['starting_time'], data['direct_unit_cost'], data['expected_operation_cost_amt'],
                data['unit_cost_per'], data['setup_time'], data['run_time']
            ))

        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        cursor.close()
