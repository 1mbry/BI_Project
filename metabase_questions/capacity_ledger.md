Capacity ledger: 
Libro contabile utilizzato per monitorare e gestire la capacità operativa di risorse all'interno di un'azienda. Questo tipo di registro è spesso impiegato in contesti di produzione o di gestione delle risorse aziendali per tenere traccia delle attività legate alla capacità di produzione e operativa.
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
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

            x Qual è la quantità media prodotta per tipo di operazione?

            Tipo di operazione: Indica la natura specifica dell'operazione di produzione, come assemblaggio, lavorazione o altre attività specifiche nel processo produttivo. (Work Center, Machine Center)

                SELECT
                    type,
                    AVG(quantity) AS quantita_media_prodotta
                FROM
                    capacity_ledger
                GROUP BY
                    type
                ORDER BY
                    quantita_media_prodotta DESC;


            x Come variano le quantità prodotte nel tempo?

                Variazione delle quantità prodotte: Questo si riferisce alle fluttuazioni o ai cambiamenti nelle quantità dei prodotti che vengono generati durante le attività di produzione. Può interessare sia le variazioni giornaliere, settimanali o mensili che quelle a lungo termine nel corso del tempo.

                Nel tempo: Si riferisce all'asse temporale, indicando che si vuole comprendere come cambiano le quantità prodotte attraverso diverse istanze temporali. Questo può includere analisi giornaliere, settimanali, mensili o anche annuali, a seconda della scala temporale di interesse.

                    SELECT
                        DATE(posting_date) AS data,
                        SUM(quantity) AS quantita_totale
                    FROM
                        capacity_ledger
                    GROUP BY
                        DATE(posting_date)
                    ORDER BY
                        data;

-----------------------------------------------------------------------------------------------------------------------------------------------
        
        Costi operativi:

            x Quali sono i costi operativi totali e medi per tipo di operazione?

                Costi operativi totali: Si riferisce all'ammontare totale dei costi operativi associati alle attività di produzione registrate nel tuo capacity ledger. Questi costi possono includere direttamente i costi e i costi generali.

                Costi operativi medi: Questo rappresenta la media dei costi operativi per ciascuna combinazione di tipo di operazione. La media viene calcolata dividendo i costi operativi totali per il numero di occorrenze (registrazioni) per ciascuna combinazione.

                SELECT
                    type,
                    SUM(direct_cost + overhead_cost) AS costi_totali,
                    AVG(direct_cost + overhead_cost) AS costi_medi
                FROM
                    capacity_ledger
                GROUP BY
                    type
                ORDER BY
                    costi_totali DESC;


            x Come variano i costi diretti e i costi indiretti nel tempo?

                Costi diretti: Si riferisce ai costi associati direttamente alla produzione di beni o servizi. Ad esempio, potrebbe includere costi di materiali, manodopera diretta e altri costi direttamente collegati alle attività produttive.

                Costi indiretti: Questi sono costi che non possono essere attribuiti direttamente a un particolare prodotto o servizio, ma sono associati alle operazioni generali dell'azienda. Questi potrebbero includere costi di gestione generale, amministrativi, manutenzione delle attrezzature e altri costi generali.

                SELECT
                    DATE(posting_date) AS data,
                    SUM(direct_cost) AS costi_diretti_totali,
                    SUM(overhead_cost) AS costi_indiretti_totali
                FROM
                    capacity_ledger
                GROUP BY
                    DATE(posting_date)
                ORDER BY
                    data;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Efficienza del tempo:

            x Qual è la percentuale di tempo di esecuzione rispetto al tempo totale per ciascuna operazione?

                Tempo di esecuzione: Si riferisce al periodo in cui effettivamente avviene l'operazione di produzione. È il tempo durante il quale la risorsa o la macchina è attivamente coinvolta nell'esecuzione dell'operazione.

                Tempo totale: Questo rappresenta l'intero periodo di tempo dedicato a un'operazione specifica, inclusi tempi di setup, tempi di esecuzione e altri possibili intervalli di tempo associati.

                Percentuale di tempo di esecuzione: La domanda chiede di esprimere il tempo di esecuzione come percentuale del tempo totale per ciascuna operazione. Questo fornisce un'indicazione di quanto tempo, in termini percentuali, è effettivamente dedicato all'esecuzione dell'operazione rispetto all'intero processo.

                SELECT
                    operation_id,
                    (SUM(run_time) / SUM(total_time)) * 100 AS percentuale_tempo_di_esecuzione
                FROM
                    capacity_ledger
                GROUP BY
                    operation_id;


            x Come variano i tempi di setup e di esecuzione nel tempo?

                Tempi di setup: Rappresentano il periodo dedicato alla preparazione e alla configurazione delle risorse (macchine, strumenti, etc.) prima di avviare effettivamente un'operazione di produzione. Questo può includere attività come il montaggio di strumenti, la configurazione di macchine, o altre attività preparatorie.

                Tempi di esecuzione: Indicano il tempo effettivamente dedicato all'esecuzione dell'operazione di produzione una volta completato il setup. Questo rappresenta il periodo in cui la risorsa o la macchina è attivamente coinvolta nell'esecuzione dell'attività produttiva.

                SELECT
                    DATE(posting_date) AS data,
                    AVG(setup_time) AS tempo_medio_setup,
                    AVG(run_time) AS tempo_medio_esecuzione
                FROM
                    capacity_ledger
                WHERE
                    setup_time IS NOT NULL AND run_time IS NOT NULL
                GROUP BY
                    DATE(posting_date)
                ORDER BY
                    data;


-----------------------------------------------------------------------------------------------------------------------------------------------

        Scarti di produzione:

            x Qual è la percentuale di scarti rispetto alla quantità totale prodotta?

                Scarti: Rappresentano i prodotti o i materiali che non soddisfano i requisiti di qualità e che vengono considerati non utilizzabili o difettosi. Gli scarti possono derivare da difetti di produzione, errori nel processo, o altri problemi.

                Quantità totale prodotta: Indica l'ammontare complessivo dei prodotti generati durante un periodo specifico o attraverso una serie di operazioni produttive.

                Percentuale di scarti: La domanda cerca di calcolare la proporzione degli scarti rispetto alla quantità totale prodotta. Questo può fornire indicazioni sulla qualità del processo produttivo e sull'efficienza nella gestione dei materiali.

                SELECT
                    SUM(scrap_quantity) / SUM(quantity) * 100 AS percentuale_scarti
                FROM
                    capacity_ledger
                WHERE
                    quantity IS NOT NULL;


            x Come variano i rifiuti nel tempo e in relazione a tipi di ordini?

                SELECT
                    DATE(posting_date) AS data,
                    type,
                    SUM(scrap_quantity) AS quantita_scarti
                FROM
                    capacity_ledger
                WHERE
                    scrap_quantity IS NOT NULL
                GROUP BY
                    DATE(posting_date), type
                ORDER BY
                    data, quantita_scarti DESC;

            
        
-----------------------------------------------------------------------------------------------------------------------------------------------
        
        Andamento delle attività nel tempo:

            x Qual è l'andamento delle attività di produzione nel corso del tempo?

                SELECT
                    DATE(posting_date) AS data,
                    SUM(quantity) AS quantita_totale,
                    AVG(run_time) AS tempo_medio_esecuzione
                FROM
                    capacity_ledger
                GROUP BY
                    DATE(posting_date)
                ORDER BY
                    data;

            x Ci sono periodi di picco o di calo dell'attività che possono essere identificati?

                Periodi di picco: Rappresentano periodi in cui l'attività di produzione raggiunge livelli massimi, con un aumento significativo della quantità di prodotti generati o delle operazioni eseguite.

                Periodi di calo: Indicano periodi in cui l'attività di produzione scende a livelli minimi, con una riduzione significativa della quantità di prodotti generati o delle operazioni eseguite.

                Identificazione: La domanda chiede se puoi identificare chiaramente questi periodi di picco o di calo analizzando i dati nel tuo capacity ledger.

                SELECT
                    DATE(posting_date) AS data,
                    SUM(quantity) AS quantita_totale
                FROM
                    capacity_ledger
                GROUP BY
                    DATE(posting_date)
                ORDER BY
                    quantita_totale DESC;

        
-----------------------------------------------------------------------------------------------------------------------------------------------

        Rapporti tra variabili:

            x Esistono correlazioni tra la quantità prodotta e i costi operativi?

                Costi operativi: Sono i costi associati alle attività operative di produzione e possono includere sia costi diretti (ad esempio, materiali e manodopera) che costi indiretti (ad esempio, spese generali).

                Correlazioni: La domanda cerca di determinare se ci sono relazioni statistiche o tendenze tra la quantità prodotta e i costi operativi. Ad esempio, un aumento della quantità prodotta potrebbe essere associato a un aumento o una diminuzione dei costi operativi.

                SELECT
                    quantity,
                    SUM(direct_cost + overhead_cost) AS costi_operativi_totali
                FROM
                    capacity_ledger
                WHERE
                    quantity IS NOT NULL
                GROUP BY
                    quantity
                ORDER BY
                    quantity;


            x Come influiscono i tempi di esecuzione sul costo totale dell'operazione?

                Tempi di esecuzione: Rappresentano il periodo di tempo durante il quale una risorsa o una macchina è attivamente coinvolta nell'esecuzione di un'operazione di produzione.

                Costo totale dell'operazione: È il costo complessivo associato a un'operazione specifica di produzione e può includere costi diretti, costi indiretti e altri costi operativi.

                Influenza: La domanda cerca di capire come i tempi di esecuzione incidano sul costo totale di un'operazione. Ad esempio, se un'operazione richiede più tempo di esecuzione, ciò potrebbe comportare un aumento dei costi operativi totali.

                SELECT
                    operation_id,
                    AVG(run_time) AS tempo_medio_esecuzione,
                    SUM(direct_cost + overhead_cost) AS costo_totale_operazione
                FROM
                    capacity_ledger
                WHERE
                    run_time IS NOT NULL
                    AND (direct_cost + overhead_cost) IS NOT NULL
                GROUP BY
                    operation_id
                ORDER BY
                    costo_totale_operazione DESC;

        
-----------------------------------------------------------------------------------------------------------------------------------------------

        Monitoraggio delle date:

            x Qual è la frequenza delle attività di produzione in base alla data di registrazione (posting_date)?

                SELECT
                    DATE(posting_date) AS data_di_registrazione,
                    COUNT(*) AS numero_di_attivita
                FROM
                    capacity_ledger
                GROUP BY
                    DATE(posting_date)
                ORDER BY
                    data_di_registrazione;


            x Ci sono giorni o periodi specifici in cui si verificano più attività?

                SELECT
                    DAYOFWEEK(posting_date) AS giorno_della_settimana,
                    COUNT(*) AS numero_di_attivita
                FROM
                    capacity_ledger
                GROUP BY
                    giorno_della_settimana
                ORDER BY
                    numero_di_attivita DESC;

                
                
                DAYOFWEEK(posting_date) restituisce il giorno della settimana corrispondente alla data di registrazione.


-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------

