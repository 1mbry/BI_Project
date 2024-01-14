# Python version 3.11.0
# requests-ntlm 1.1.0
# mysql-connector-python 8.2.0

import requests
from requests_ntlm import HttpNtlmAuth
from db.db import (
    establish_mysql_connection,
    establish_db_connection,
    does_database_exist, 
    create_database, 
    do_tables_exist,
    create_tables
)
from db.update_db import (
    update_itemLedgerEntries,
    update_capacityledgerentries,
    update_productionorders,
    update_machinecenters,
    update_items,
    update_prodorderroutinglines
)

# URL per gli Odata Services
base_url = 'http://localhost:7048/BC210'

# Le mie credenziali
username = 'ICTS22-24.319' 
password = 'Service2024!'
domain = 'STUDENTI'

# Specifico che come output voglio un json
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

# Enpoints delle API
endpoints = {
    '/api/provision/production/v1.0/itemledgerentries' : update_itemLedgerEntries, 
    '/api/provision/production/v1.0/capacityledgerentries' : update_capacityledgerentries, 
    '/api/provision/production/v2.0/productionorders' : update_productionorders, 
    '/api/provision/production/v1.0/machinecenters' : update_machinecenters, 
    '/api/provision/production/v1.0/items': update_items, 
    '/api/provision/production/v2.0/prodorderroutinglines' : update_prodorderroutinglines
}

# Metodo per effettuare l'autenticazione a Business Central
def ntlm_authentication(username, password, domain):
    auth = HttpNtlmAuth(f"{domain}\\{username}", password)
    return auth

# Metodo per richiedere i JSON 
def request_api_data(api_url, auth, headers):
    try:
        response = requests.get(api_url, auth=auth, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return f"Request failed with status code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Request Exception: {e}"

# Metodo per fare l'update dei dati nel data warehouse
def update_database_with_api_data(base_url, username, password, domain, endpoints, conn):
    auth = ntlm_authentication(username, password, domain)
    
    for endpoint in endpoints:
        url = base_url + endpoint
        result = request_api_data(url, auth, headers)
        if endpoint in endpoints:
            # Esegui l'aggiornamento della tabella specifica del database usando il dizionario di funzioni
            endpoints[endpoint](conn, result)

    print("Update delle tabelle eseguito")    

# Metodo main che esegue i vari metodi per verificare, creare e aggiornare il database.
def main():
    mysql_conn = establish_mysql_connection('localhost', 'root', '')

    if not does_database_exist(mysql_conn, 'laboratorio'):
        create_database(mysql_conn,'laboratorio')

    if mysql_conn.is_connected():
        mysql_conn.close()
        print('Connessione a MySQL chiusa')

    conn = establish_db_connection('localhost', 'root', '', 'laboratorio')
    
    if not do_tables_exist(conn):
        conn = create_tables(conn)

    update_database_with_api_data(base_url, username, password, domain, endpoints, conn)
    
    if conn.is_connected():
        conn.close()
        print('Connessione a laboratorio chiusa')
