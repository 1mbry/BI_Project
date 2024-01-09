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


#def update_capacityledgerentries

#def update_productionorders

#def update_machinecenters

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

#def update_prodorderroutinglines