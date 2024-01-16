Machine Centers: 

    sembra essere una parte di un sistema o di un database che gestisce informazioni relative a centri di lavoro o macchine in un contesto produttivo o operativo. 

    id: Identificatore univoco per ciascun centro di lavoro. Questo campo è spesso utilizzato come chiave primaria e può essere incrementato automaticamente (AUTO_INCREMENT).

    no: Un campo di tipo VARCHAR(255) che sembra rappresentare un numero o un codice univoco associato al centro di lavoro.

    name: Un campo di tipo VARCHAR(255) che rappresenta il nome del centro di lavoro.


-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
        Analisi della distribuzione dei nomi dei centri di lavoro:

            Domanda: Qual è la distribuzione dei nomi dei centri di lavoro nella tabella machine_centers?
            SQL Query:

            SELECT name, COUNT(*) AS conteggio
            FROM machine_centers
            GROUP BY name
            ORDER BY conteggio DESC;

-----------------------------------------------------------------------------------------------------------------------------------------------
        
        Conteggio totale dei centri di lavoro:

            Domanda: Quanti centri di lavoro sono presenti nella tabella machine_centers?
            SQL Query:

            SELECT COUNT(*) AS numero_centri_di_lavoro
            FROM machine_centers;

-----------------------------------------------------------------------------------------------------------------------------------------------

        Identificazione dei centri di lavoro con nomi duplicati:

            Domanda: Ci sono centri di lavoro con nomi duplicati nella tabella?
            SQL Query:

            SELECT name, COUNT(*) AS conteggio
            FROM machine_centers
            GROUP BY name
            HAVING conteggio > 1;


-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------

