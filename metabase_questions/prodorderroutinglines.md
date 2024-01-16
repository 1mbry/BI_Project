Prod Order Routinglines: 

        Orientata alle operazioni di produzione: Questa tabella sembra essere focalizzata sul tracciare informazioni dettagliate relative alle operazioni di produzione, incluse le attività specifiche associate a un ordine di produzione, il percorso di produzione, il centro di lavoro coinvolto e i tempi e costi associati a ciascuna operazione.

        Collegata agli ordini di produzione: Ogni riga sembra essere associata a un ordine di produzione specifico (prodorder_no), indicando che si tratta di dati relativi all'esecuzione di ordini di produzione.

        Registra tempi e costi operativi: Include informazioni dettagliate sui tempi di setup (setup_time), tempi di esecuzione (run_time), costi unitari diretti (direct_unit_cost), costi attesi dell'operazione (expected_operation_cost_amt), e altri dettagli specifici delle operazioni.

    Invece la Tabella capacity_ledger:

        Orientata alla capacità di produzione: Questa tabella sembra essere progettata per registrare informazioni relative alla capacità di produzione complessiva, inclusi dati su quantità prodotte, tempi di esecuzione, costi diretti e indiretti, ecc.

        Maggiore aggregazione di dati: I dati sembrano essere più aggregati e potrebbero essere destinati a fornire una visione più generale della capacità e delle prestazioni di produzione, piuttosto che concentrarsi su operazioni specifiche come nella tabella prodorderroutinglines.

        Registro di attività di produzione generale: Include dettagli come il tipo di ordine, il tipo di attività, la quantità totale, la quantità di produzione, i tempi di inizio e fine, i costi generali, ecc.

    In sintesi, mentre entrambe le tabelle sono coinvolte nella gestione delle attività di produzione, la tabella prodorderroutinglines sembra concentrarsi su dettagli operativi specifici relativi alle singole operazioni in un ordine di produzione, mentre la tabella capacity_ledger sembra fornire una visione più aggregata delle attività di produzione in termini di capacità e risorse utilizzate. La scelta di utilizzare una tabella rispetto all'altra dipenderà dal livello di dettaglio richiesto nelle analisi di business specifiche.

        id: Identificatore univoco per ciascuna riga nella tabella. Solitamente, questo campo funge da chiave primaria e può essere incrementato automaticamente (AUTO_INCREMENT).

        operation_no: Numero associato a una specifica operazione o attività.

        type: Tipo specifico di operazione o attività.

        no: Numero univoco associato all'operazione.

        status: Stato corrente dell'operazione (ad esempio, in corso, completato, ecc.).

        prodorder_no: Numero di ordine di produzione associato all'operazione.

        description: Descrizione dell'operazione.

        routing_no: Numero associato al percorso di produzione o al flusso di lavoro.

        work_center_no: Numero associato al centro di lavoro in cui viene svolta l'operazione.

        starting_date: Data di inizio dell'operazione.

        starting_time: Ora di inizio dell'operazione.

        direct_unit_cost: Costo unitario diretto associato all'operazione.

        expected_operation_cost_amt: Costo atteso dell'operazione.

        unit_cost_per: Costo unitario per un'unità dell'operazione.

        setup_time: Tempo necessario per la preparazione dell'operazione.

        run_time: Tempo di esecuzione dell'operazione.

-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
        Analisi della distribuzione dei tipi di operazioni:

            Domanda: Qual è la distribuzione dei tipi di operazioni nella tabella prodorderroutinglines?
            Query SQL:

            SELECT type, COUNT(*) AS conteggio
            FROM prodorderroutinglines
            GROUP BY type
            ORDER BY conteggio DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------
        
        Conteggio totale delle operazioni per tipo di stato:

            Domanda: Quanti record ci sono per ciascun stato nella tabella prodorderroutinglines?
            Query SQL:

            SELECT status, COUNT(*) AS conteggio
            FROM prodorderroutinglines
            GROUP BY status;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi dei costi diretti delle operazioni:

            Domanda: Qual è la distribuzione dei costi diretti delle operazioni?
            Query SQL:

            SELECT operation_no, AVG(direct_unit_cost) AS costo_unitario_medio
            FROM prodorderroutinglines
            GROUP BY operation_no
            ORDER BY costo_unitario_medio DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi dei tempi di setup e di esecuzione per tipo di operazione:

            Domanda: Qual è la durata media di setup e di esecuzione per ciascun tipo di operazione?
            Query SQL:

            SELECT type, AVG(setup_time) AS tempo_medio_setup, AVG(run_time) AS tempo_medio_esecuzione
            FROM prodorderroutinglines
            GROUP BY type
            ORDER BY type;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Analisi dei tempi di setup e di esecuzione in base al centro di lavoro:

            Domanda: Qual è la durata media di setup e di esecuzione per ciascun centro di lavoro?
            Query SQL:

            SELECT work_center_no, AVG(setup_time) AS tempo_medio_setup, AVG(run_time) AS tempo_medio_esecuzione
            FROM prodorderroutinglines
            GROUP BY work_center_no
            ORDER BY work_center_no;

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

