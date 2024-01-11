Metabase domande: c'è la query SQL per riferimento
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------	Capacity ledger: registro delle attività

        Analisi temporale:

            x Qual è la distribuzione temporale delle attività di produzione nel capacity ledger?
                 Ovvero come le attività di produzione sono distribuite nel tempo, se ci sono periodi di picco o di calo, e come questa distribuzione può influire sull'utilizzo delle risorse o sulla pianificazione delle attività produttive. 
                
                SELECT
                    DATE(starting_time) AS data,
                    COUNT(*) AS attivita_totale
                FROM
                    capacity_ledger
                GROUP BY
                    DATE(starting_time)
                ORDER BY
                    data;



            x Quali sono gli intervalli di tempo più frequenti per le operazioni di setup e di runtime?
                Ovvero quali sono gli intervalli temporali più comuni durante i quali si verificano le attività di setup e di runtime, permettendo di comprendere meglio la distribuzione temporale di queste operazioni. L'obiettivo potrebbe essere ottimizzare la pianificazione delle attività in base ai periodi in cui le risorse sono più frequentemente coinvolte in setup o runtime.

                Nota bene:

                    Setup: Il tempo necessario per preparare e configurare le risorse (macchine, strumenti, ecc.) prima di iniziare effettivamente l'operazione di produzione.
                    
                    Runtime: Il tempo effettivo dedicato all'esecuzione dell'operazione di produzione una volta che il setup è completato.
        
                SELECT
                    HOUR(starting_time) AS ora_inizio,
                    AVG(setup_time) AS tempo_medio_setup,
                    AVG(run_time) AS tempo_medio_runtime,
                    COUNT(*) AS numero_di_operazioni
                FROM
                    capacity_ledger
                WHERE
                    setup_time IS NOT NULL AND run_time IS NOT NULL
                GROUP BY
                    ora_inizio
                ORDER BY
                    numero_di_operazioni DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------
        
        Performance delle risorse:

            x Quali risorse (routing_no) sono utilizzate più frequentemente o richiedono più tempo di setup?

                Risorse (routing_no): Si riferisce alle entità o alle risorse coinvolte nel processo produttivo, ciascuna identificata da un codice o un numero di routing ("routing_no"). Queste risorse potrebbero essere macchine, stazioni di lavoro o altri elementi che contribuiscono al completamento di un'operazione.

                SELECT
                    routing_no,
                    COUNT(*) AS numero_di_operazioni,
                    AVG(setup_time) AS tempo_medio_setup
                FROM
                    capacity_ledger
                WHERE
                    setup_time IS NOT NULL
                GROUP BY
                    routing_no
                ORDER BY
                    numero_di_operazioni DESC, tempo_medio_setup DESC;

                Con questa query, otterrai una lista di risorse con il numero totale di operazioni e il tempo medio di setup per ciascuna risorsa, consentendoti di identificare quelle più frequentemente utilizzate o con tempi di setup più lunghi.



            x Quali risorse hanno la migliore e la peggiore efficienza in termini di tempo di esecuzione?

                Efficienza in termini di tempo di esecuzione: Si riferisce a quanto tempo una risorsa impiega per completare un'operazione di produzione. In questa domanda, si è interessati a individuare le risorse che sono efficienti, cioè quelle che completano le operazioni in meno tempo, e quelle meno efficienti, che richiedono più tempo per le operazioni.

                SELECT
                    routing_no,
                    AVG(run_time) AS tempo_medio_esecuzione
                FROM
                    capacity_ledger
                WHERE
                    run_time IS NOT NULL
                GROUP BY
                    routing_no
                ORDER BY
                    tempo_medio_esecuzione ASC;

        Dopo aver eseguito questa query, potrai identificare facilmente le risorse con il tempo di esecuzione più breve e più lungo. Le risorse con tempi di esecuzione più brevi possono essere considerate le più efficienti, mentre quelle con tempi più lunghi possono richiedere ulteriori analisi o ottimizzazioni per migliorare l'efficienza del processo produttivo.

-----------------------------------------------------------------------------------------------------------------------------------------------
        
        Quantità prodotte:

            Qual è la quantità media prodotta per tipo di ordine e per tipo di operazione?
            Come variano le quantità prodotte nel tempo?

-----------------------------------------------------------------------------------------------------------------------------------------------
        
        Costi operativi:

            Quali sono i costi operativi totali e medi per tipo di ordine e tipo di operazione?
            Come variano i costi diretti e i costi indiretti nel tempo?
        
-----------------------------------------------------------------------------------------------------------------------------------------------

        Efficienza del tempo:

            Qual è la percentuale di tempo di esecuzione rispetto al tempo totale per ciascuna operazione?
            Come variano i tempi di setup e di esecuzione nel tempo?

-----------------------------------------------------------------------------------------------------------------------------------------------

        Scarti di produzione:

            Qual è la percentuale di scarti rispetto alla quantità totale prodotta?
            Come variano i rifiuti nel tempo e in relazione a tipi specifici di ordini?
        
-----------------------------------------------------------------------------------------------------------------------------------------------
        
        Andamento delle attività nel tempo:

            Qual è l'andamento delle attività di produzione nel corso del tempo?
            Ci sono periodi di picco o di calo dell'attività che possono essere identificati?
        
-----------------------------------------------------------------------------------------------------------------------------------------------

        Rapporti tra variabili:

            Esistono correlazioni tra la quantità prodotta e i costi operativi?
            Come influiscono i tempi di esecuzione sul costo totale dell'operazione?
        
-----------------------------------------------------------------------------------------------------------------------------------------------

        Monitoraggio delle date:

            Qual è la frequenza delle attività di produzione in base alla data di registrazione (posting_date)?
            Ci sono giorni o periodi specifici in cui si verificano più attività?

-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------

