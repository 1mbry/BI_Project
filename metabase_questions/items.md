Items: 

    id: Un identificatore univoco per ogni record nella tabella, incrementato automaticamente (AUTO_INCREMENT), spesso utilizzato come chiave primaria.

    no: Una colonna di tipo VARCHAR(255), che probabilmente contiene un numero o codice univoco associato all'articolo.

    description: Una colonna di tipo VARCHAR(255), che contiene una descrizione dell'articolo.

    routing_no: Una colonna di tipo VARCHAR(255), che potrebbe rappresentare un numero di instradamento o un codice associato al processo di produzione dell'articolo.

    production_bom_no: Una colonna di tipo VARCHAR(255), che potrebbe contenere un numero di lista dei materiali (Bill of Materials - BOM) associato alla produzione dell'articolo.

    Questa struttura di tabella è progettata per memorizzare informazioni dettagliate sugli articoli, inclusi identificatori univoci, descrizioni, informazioni di produzione e collegamenti a processi specifici. Con queste informazioni, è possibile analizzare e gestire gli articoli all'interno di un contesto aziendale, soprattutto in ambito produttivo o logistico.
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
        Analisi delle categorie di articoli:

            Domanda: Quante categorie uniche di articoli ci sono basate sulla routing_no?
            SQL Query:

                SELECT COUNT(DISTINCT routing_no) AS numero_categorie FROM items;


-----------------------------------------------------------------------------------------------------------------------------------------------

        Top 10 articoli per produzione:

            Domanda: Quali sono i primi 10 articoli per quantità prodotta?
            SQL Query:

                SELECT 
                    no, 
                    description, 
                    SUM(quantity) AS quantita_totale
                FROM 
                    items
                JOIN 
                    capacity_ledger ON items.id = capacity_ledger.item_no
                GROUP BY 
                    items.id, 
                    no, 
                    description
                ORDER BY 
                    quantita_totale DESC
                LIMIT 10;



-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi della distribuzione delle descrizioni:

            Domanda: Qual è la distribuzione delle descrizioni degli articoli?
            SQL Query:

                SELECT 
                    description, 
                    COUNT(*) AS conteggio
                FROM 
                    items
                GROUP BY 
                    description
                ORDER BY 
                    conteggio DESC;



-----------------------------------------------------------------------------------------------------------------------------------------------

        Identificazione degli articoli senza informazioni di produzione:

            Domanda: Quali articoli non hanno informazioni associate nella tabella capacity_ledger?
            SQL Query:

                SELECT 
                    id, 
                    no, 
                    description
                FROM 
                    items
                WHERE 
                    id NOT IN (SELECT DISTINCT item_no FROM capacity_ledger);



-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi della correlazione tra produzione e componenti:

            Domanda: C'è una correlazione tra la produzione di un articolo e la presenza di componenti nella production_bom_no?
            SQL Query:

                SELECT 
                    production_bom_no, 
                    AVG(quantity) AS media_quantita_prodotta
                FROM 
                    items
                JOIN 
                    capacity_ledger ON items.id = capacity_ledger.item_no
                GROUP BY 
                    production_bom_no;



-----------------------------------------------------------------------------------------------------------------------------------------------

        Visualizzazione degli articoli più comuni per tipo di ordine:

            Domanda: Quali sono gli articoli più comuni per ciascun tipo di ordine?
            SQL Query:

                SELECT 
                    order_type, 
                    no, 
                    description, 
                    COUNT(*) AS conteggio
                FROM 
                    items
                JOIN 
                    capacity_ledger ON items.id = capacity_ledger.item_no
                GROUP BY 
                    order_type, 
                    no, 
                    description
                ORDER BY 
                    order_type, 
                    conteggio DESC;


-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi della frequenza delle attività di produzione per articolo:

            Domanda: Qual è la frequenza delle attività di produzione per ciascun articolo?
            SQL Query:

                SELECT 
                    items.id, 
                    no, 
                    description, 
                    COUNT(*) AS frequenza_attivita
                FROM 
                    items
                JOIN 
                    capacity_ledger ON items.id = capacity_ledger.item_no
                GROUP BY 
                    items.id, 
                    no, 
                    description
                ORDER BY 
                    frequenza_attivita DESC;



-----------------------------------------------------------------------------------------------------------------------------------------------

        Conteggio degli articoli senza descrizione:

            Domanda: Quanti articoli non hanno una descrizione associata?
            SQL Query:

                SELECT 
                    COUNT(*) AS numero_articoli_senza_descrizione
                FROM 
                    items
                WHERE 
                    description IS NULL OR description = '';



-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------

