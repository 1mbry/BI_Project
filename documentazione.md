# Documentazione dell'ETL

L'obiettivo di questo progetto è automatizzare il processo di aggiornamento di un Data Warehouse tramite l'estrazione di dati da un sistema di gestione aziendale, in particolare da Microsoft Dynamics 365 Business Central. Gli script sviluppati in Python gestiscono l'intera pipeline, dalla richiesta di dati alle API di Business Central fino all'aggiornamento delle tabelle del Data Warehouse.

## Struttura dell'ETL

### 1. main.py

È lo script principale del progetto ed è responsabile dell'orchestrazione generale delle attività di aggiornamento del Data Warehouse.

#### Dipendenze
- **'schedule'**: La libreria **schedule** viene utilizzata per la pianificazione delle attività all'interno dello script.
- **'time'**: La libreria **time** è utilizzata per introdurre ritardi temporali durante l'esecuzione dello script.
- **'auth'**: Modulo che importa la funzione **'main'** da **'auth.py'**

#### Variabili Globali
- **'stop_jobs'**: Flag booleano utilizzato per indicare se l'esecuzione delle attività deve essere interrotta.

#### Metodi
1. **'__main__'**:
    - Invoca il metodo **'main'** al momento dell'esecuzione diretta del file.
2. **'main'**  
    - Metodo principale che gestisce la pianificazione delle attività e l'esecuzione continua dello script.
    - Pianifica l'esecuzione dello script ogni giorno alle 01:00 utilizzando la libreria **'schedule'**
    - Utilizza un loop per eseguire continuamente il programma, eseguendo le attività pianificate fino a quando la variabile **'stop_jobs'** diventa **'True'**.
    - Presenta un blocco di eccezioni per gestire l'interruzione dell'applicazione da parte dell'utente attraverso la combinazione di tasti (CTRL + C).
3. **'run_jobs'**
    - Metodo responsabile di richiamare la funzione principale (**'main'**) presente nel modulo **'auth'**.
    - Questo metodo è la parte iniziale del flusso di lavoro, garantendo che l'ETL sia autenticato con successo prima di eseguire le attività di raccolta dati.
4. **'stop_schedule'**:
    - Metodo invocato al momento dell'interruzione del programma. Imposta la variabile **'stop_jobs'** su **'True'**, cancella le esecuzioni pianificate e termina l'esecuzione dello script.

### 2. Cartella: 'auth'

La cartella **'auth'** contiene il modulo  auth.py che gestisce l'autenticazione con Business Central.

### auth.py

Il file **'auth.py'** gestisce l'autenticazione con il sistema Business Central. L'autenticazione è richiesta da Business Central per assicurare che solo gli utenti autorizzati possano accedere ai suoi dati.

#### Dipendenze
- **'requests'**: La libreria **'requests'** viene utilizzata per effettuare richieste HTTP alle API di Business Central.
- **'requests_ntlm'**: La libreria **'requests_ntlm'** fornisce l'autenticazione NTLM per le richieste alle API.
- **'db'**: Modulo contenente funzioni per la gestione del database MySQL.
- **'update_db'**: Modulo con funzioni specifiche per l'aggiornamento delle tabelle del database.

#### Variabili Globali
- **'base_url'**: URL base per gli OData Services di Business Central.
- Credenziali per l'autenticazione NTLM:
    - **'username'**: Nome utente windows.
    - **'password'**: Password windows.
    - **'domain'**: Dominio.
- Intestazioni per le richieste HTTP:
    - **'headers'**: Contiene il tipo di contenuto e l'accettazione del formato JSON.
- Endpoints delle API di Business Central:
    - **'enpoints'**: Dizionario che mappa gli enpoint API alle funzioni di aggiornamento corrispondenti nel modulo **'update_db'**.

#### Metodi
1. **'main'**: 
    -  Metodo principale che gestisce la connessione al database, verifica l'esistenza del database e delle tabelle, esegue l'aggiornamento dei dati e chiude le connessioni.
2. **'ntlm_authentication(username, password, domain)'**:
    - Metodo per effettuare l'autenticazione NTLM con le credenziali fornite.
3. **'request_api_data(api_url, auth, headers)'**: 
    - Metodo per effettuare una richiesta alle API di Business Central e ottenere i dati.
4. **'update_database_with_api_data(base_url, username, password, domain, endpoints, conn)'**: 
    - Metodo principipale che itera sugli enpoints delle API di Business Central.
    - Richiede i dati da ciascun endpoint e aggiorna le tabelle del database corrispondenti utilizzando il modulo **'update_db'**.
    
### 3. Cartella: 'db'

La cartella **'db'** contiene il modulo **'db.py'** che gestisce la connessione con MySQL  e **'update_db.py'** che gestisce l'aggiornamento delle tabelle del database.

### db.py

Il modulo **'db.py'** gestisce la connessione al data warehouse MySQL e fornisce metodi per la gestione del database "laboratorio", inclusi il controllo dell'esistenza, la creazione e la gestione delle tabelle.

#### Dipendenze
- **'mysql.connector'**: La libreria **'mysql.connector'** è utilizzata per la connessione e le operazioni nel database MySQL.

#### Metodi
1. **'establish_mysql_connection(host, user, password)'**:
    - Questo metodo stabilisce la connessione al data warehouse MySQL.
    - Restituisce l'oggetto di connessione a MySQL
2. **'establish_db_connection(host, user, password, database_name)'**:
    - Questo metodo stabilisce la connessione al database "laboratorio".
    - Restituisce l'oggetto di connessione al database "laboratorio".
3. **'does_database_exist(conn, database_name)'**:
    - Questo metodo verifica se il database "laboratorio" esiste.
    - Restituisce True se il database esiste, altrimenti False.
4. **'create_database(conn, database_name)'**:
    - Questo metodo crea il database "laboratorio".
5. **'do_tables_exist(conn)'**:
    - Questo metodo verifica se le tabelle necessarie esistono nel database "laboratorio".
    - Restituisce True se le tabelle esistono, altrimenti False.
6. **'create_tables(conn)'**:
    - Questo metodo crea le tabelle nel database "laboratorio".
    - Restituisce l'oggetto di connessione aggiornato dopo la creazione delle tabelle.

### update_db.py
Il modulo **'update_db.py'** gestisce le operazioni di aggiornamento del database, incluse le funzioni per l'aggiornamento di specifiche tabelle con dati provenienti dalle API di Business Central. Le funzioni presenti in questo modulo vengono utilizzate per inserire o aggiornare le informazioni all'interno delle tabelle del database "laboratorio".

#### Dipendenze
- **'mysql.connector'**: La libreria **'mysql.connector'** è utilizzata per la connessione e le operazioni nel database MySQL.

#### Metodi
1. **'update_itemLedgerEntries(conn, data)'**:
    - Aggiorna la tabella itemledgerentries con i dati forniti.
2. **'update_capacityledgerentries(conn, data)'**:
    - Aggiorna la tabella capacityledgerentries con i dati forniti.
3. **'update_productionorders(conn, data)'**:
    - Aggiorna la tabella productionorders con i dati forniti.
4. **'update_machinecenters(conn, data)'**:
    - Aggiorna la tabella machinecenters con i dati forniti.
5. **'update_items(conn, data)'**:
    - Aggiorna la tabella items con i dati forniti.
6. **'update_prodorderroutinglines(conn, data)'**:
    - Aggiorna la tabella prodorderroutinglines con i dati forniti.

### Utilizzo e Configurazione
1. **Installre le Dipendenze**:
- Assicurarsi che le librerie necessarie siano installate.
2. **Configurazione delle Credenziali**:
- Modificare le credenziali di autenticazione in **'auth/auth.py'** per garantire l'accesso a Business Central.
3. **Configurazione del Database**:
- Assicurarsi che il database MySQL sia correttamente configurato con le tabelle necessarie. Modificare eventualmente la connessione del database in **'db/db.py'** se necessario.
4. Esecuzione dello Script:
- Eseguire **'main.py'** per avviare il processo ETL. L'esecuzione sarà automaticamente schedulata ogni giorno alle ore 01:00, ma è possibile personalizzare questa pianificazione a seconda delle esigenze.

