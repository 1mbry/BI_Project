Item ledger: 

    Rappresenta generalmente un registro (ledger) di transazioni o voci contabili specificamente associate agli articoli o prodotti in un sistema contabile o di gestione aziendale. In un contesto aziendale, l'item_ledger tiene traccia delle movimentazioni e delle transazioni relative agli articoli, registrando cambiamenti nella quantità degli articoli, i costi associati e altre informazioni pertinenti.

    Nella definizione della tua tabella item_ledger, la struttura suggerisce che ogni voce nel registro rappresenta una transazione o una registrazione specifica associata a un articolo. Ecco una breve spiegazione dei campi principali della tabella:

    id: Identificatore univoco per ciascuna voce nel ledger.
    entry_no: Numero di registrazione associato alla transazione.
    entry_type: Tipo di transazione (ad esempio, acquisto, vendita, trasferimento, ecc.).
    item_no: Numero o identificatore dell'articolo associato alla transazione.
    document_no: Numero di documento associato alla transazione (ad esempio, numero di fattura).
    quantity: Quantità dell'articolo coinvolta nella transazione (positiva o negativa a seconda dell'operazione).
    posting_date: Data in cui la transazione è stata registrata.
    cost_amount_actual: Costo effettivo associato all'articolo nella transazione.
    
    L'item_ledger è fondamentale per la gestione degli stock, la contabilità e l'analisi delle transazioni relative agli articoli. Esso consente di tracciare movimenti di magazzino, costi associati, e fornisce una visione dettagliata delle attività relative agli articoli nel tempo. La tabella item_ledger può essere utilizzata per monitorare l'inventario, calcolare i costi medi, analizzare le transazioni di acquisto e vendita, e svolgere altre attività di business intelligence e contabilità.
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
        Analisi della distribuzione dei tipi di transazione:

            Domanda: Qual è la distribuzione dei tipi di transazione nella tabella item_ledger?
            SQL Query:

            SELECT entry_type, COUNT(*) AS conteggio
            FROM item_ledger
            GROUP BY entry_type
            ORDER BY conteggio DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------
        
        Conteggio delle transazioni per articolo:

            Domanda: Quante transazioni sono presenti per ciascun articolo nella tabella item_ledger?
            SQL Query:

            SELECT item_no, COUNT(*) AS conteggio_transazioni
            FROM item_ledger
            GROUP BY item_no
            ORDER BY conteggio_transazioni DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi della quantità media delle transazioni:

            Domanda: Qual è la quantità media delle transazioni nella tabella item_ledger?
            SQL Query:

            SELECT AVG(quantity) AS quantita_media
            FROM item_ledger;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Visualizzazione delle transazioni con quantità negative:

            Domanda: Quali transazioni hanno quantità negative?
            SQL Query:

            SELECT *
            FROM item_ledger
            WHERE quantity < 0;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi del costo totale effettivo per articolo:

            Domanda: Qual è il costo totale effettivo per ciascun articolo nella tabella item_ledger?
            SQL Query:

            SELECT item_no, SUM(cost_amount_actual) AS costo_totale_effettivo
            FROM item_ledger
            GROUP BY item_no
            ORDER BY costo_totale_effettivo DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Visualizzazione delle transazioni per tipo di documento:

            Domanda: Quali sono le transazioni associate a un tipo specifico di documento?
            SQL Query:

            SELECT document_no, entry_type, COUNT(*) AS conteggio
            FROM item_ledger
            GROUP BY document_no, entry_type
            ORDER BY conteggio DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi della quantità media e del costo per tipo di transazione:

            Domanda: Qual è la quantità media e il costo totale effettivo per ciascun tipo di transazione?
            SQL Query:

            SELECT entry_type, AVG(quantity) AS quantita_media, SUM(cost_amount_actual) AS costo_totale_effettivo
            FROM item_ledger
            GROUP BY entry_type
            ORDER BY entry_type;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Visualizzazione delle transazioni in una data specifica:

            Domanda: Quali sono le transazioni registrate in una data specifica?
            SQL Query:

            SELECT *
            FROM item_ledger
            WHERE posting_date = 'data_specifica';

-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi della quantità media di transazioni per tipo di documento:

            Domanda: Qual è la quantità media di transazioni per ciascun tipo di documento?
            SQL Query:

            SELECT document_no, AVG(quantity) AS quantita_media
            FROM item_ledger
            GROUP BY document_no
            ORDER BY quantita_media DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Conteggio delle transazioni senza quantità specificata:

            Domanda: Quante transazioni non hanno una quantità specificata?
            SQL Query:

            SELECT COUNT(*) AS numero_transazioni_senza_quantita
            FROM item_ledger
            WHERE quantity IS NULL;


-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------

