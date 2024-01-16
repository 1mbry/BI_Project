# Python version 3.11.0
# requests-ntlm 1.1.0
# mysql-connector-python 8.2.0

import requests
import mysql.connector
from requests_ntlm import HttpNtlmAuth
from db.update_db import update_itemLedgerEntries, update_items

# URL per gli Odata Services
base_url = 'http://localhost:7048/BC210'

# Le mie credenziali
username = 'windows_user' 
password = 'windows_password'
domain = 'windows_domain'

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

endpoints = {
    '/api/v2.0/itemLedgerEntries' : update_itemLedgerEntries, #funziona
    #'/api/v2.0/capacityledgerentries', #non funziona
    #'/api/v2.0/productionorders', #non funziona
    #'/api/v2.0/machinecenters', #non funziona
    '/api/v2.0/items': update_items, #funziona
    #'/api/v2.0/prodorderroutinglines' #non funziona
}

def establish_db_connection(host, user, password, database_name):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )
        return connection
    except mysql.connector.Error as error:
        print("Error:", error)
        return None

def ntlm_authentication(username, password, domain):
    auth = HttpNtlmAuth(f"{domain}\\{username}", password)
    return auth

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
    
def update_database_with_api_data(base_url, username, password, domain, endpoints, conn):
    auth = ntlm_authentication(username, password, domain)
    
    for endpoint in endpoints:
        url = base_url + endpoint
        result = request_api_data(url, auth, headers)

        if endpoint in endpoints:
            # Esegui l'aggiornamento del database specifico per l'endpoint usando il dizionario di funzioni
            endpoints[endpoint](conn, result)

def main():
    conn = establish_db_connection('localhost', 'root', '', 'laboratorio')
    update_database_with_api_data(base_url, username, password, domain, endpoints, conn)
    conn.close()
