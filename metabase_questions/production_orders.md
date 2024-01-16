Production Orders: 

        Progettata per tracciare informazioni dettagliate sugli ordini di produzione, inclusi dettagli come il numero di ordine, lo stato, la descrizione, la data di creazione, la quantità richiesta, la fonte, l'operatore assegnato e le date e orari previsti per l'esecuzione dell'ordine di produzione.

            id: Identificatore univoco per ciascuna riga nella tabella. Solitamente, questo campo funge da chiave primaria e può essere incrementato automaticamente (AUTO_INCREMENT).

            no: Numero associato all'ordine di produzione. Ogni ordine di produzione avrà un numero univoco.

            status: Stato corrente dell'ordine di produzione (ad esempio, in corso, completato, ecc.).

            description: Descrizione dell'ordine di produzione.

            creation_date: Data in cui è stato creato l'ordine di produzione.

            quantity: Quantità richiesta nell'ordine di produzione.

            source_no: Numero associato alla fonte dell'ordine di produzione.

            assigned_worker: Lavoratore o operatore assegnato all'esecuzione dell'ordine di produzione.

            due_date: Data di scadenza prevista per l'ordine di produzione.

            starting_date: Data prevista di inizio dell'ordine di produzione.

            ending_date: Data prevista di completamento dell'ordine di produzione.

            starting_time: Ora di inizio prevista dell'ordine di produzione.

            ending_time: Ora di fine prevista dell'ordine di produzione.

-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
        Analisi della distribuzione degli stati degli ordini di produzione:

            Domanda: Qual è la distribuzione degli stati degli ordini di produzione?
            Query SQL:

            SELECT status, COUNT(*) AS conteggio
            FROM production_orders
            GROUP BY status
            ORDER BY conteggio DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------
        
        Conteggio totale degli ordini di produzione per data di creazione:

            Domanda: Quanti ordini di produzione sono stati creati in ciascuna data?
            Query SQL:

            SELECT creation_date, COUNT(*) AS conteggio
            FROM production_orders
            GROUP BY creation_date
            ORDER BY creation_date;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi delle quantità ordinate per tipo di stato:

            Domanda: Qual è la somma delle quantità ordinate per ciascun tipo di stato degli ordini di produzione?
            Query SQL:

            SELECT status, SUM(quantity) AS quantita_totale
            FROM production_orders
            GROUP BY status
            ORDER BY quantita_totale DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi della distribuzione delle date di scadenza:

            Domanda: Qual è la distribuzione delle date di scadenza degli ordini di produzione?
            Query SQL:

            SELECT due_date, COUNT(*) AS conteggio
            FROM production_orders
            GROUP BY due_date
            ORDER BY conteggio DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi delle quantità ordinate per fonte:

            Domanda: Qual è la quantità totale ordinata per ciascuna fonte degli ordini di produzione?
            Query SQL:

            SELECT source_no, SUM(quantity) AS quantita_totale
            FROM production_orders
            GROUP BY source_no
            ORDER BY quantita_totale DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi del costo totale delle operazioni per ordine di produzione:

            Domanda: Qual è il costo totale delle operazioni per ciascun ordine di produzione?
            Query SQL:

            SELECT prodorder_no, SUM(direct_unit_cost) AS costo_totale
            FROM prodorderroutinglines
            GROUP BY prodorder_no
            ORDER BY costo_totale DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi del costo atteso medio delle operazioni:

            Domanda: Qual è il costo atteso medio delle operazioni?
            Query SQL:

            SELECT AVG(expected_operation_cost_amt) AS costo_atteso_medio
            FROM prodorderroutinglines;


-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------

