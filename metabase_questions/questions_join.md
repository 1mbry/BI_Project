Questions chee usano le JOIN

    Analisi del costo totale delle operazioni per ordine di produzione:

            Domanda: Qual è il costo totale delle operazioni per ciascun ordine di produzione?

            Utilità per il Cliente: Fornisce una visione consolidata dei costi totali associati a ciascun ordine di produzione, aiutando il cliente a valutare l'efficienza finanziaria e identificare aree di ottimizzazione.

            Query SQL:


            SELECT prl.prodorder_no, SUM(cl.direct_cost + cl.overhead_cost) AS costo_totale
            FROM prodorderroutinglines prl
            JOIN capacity_ledger cl ON prl.routing_no = cl.routing_no
            GROUP BY prl.prodorder_no
            ORDER BY costo_totale DESC;




    Analisi delle quantità prodotte per tipo di ordine e tipo di operazione:

            Domanda: Qual è la quantità media prodotta per tipo di ordine e tipo di operazione?

            Utilità per il Cliente: Offre una panoramica della produzione in base a tipologie di ordine e operazione, aiutando il cliente a monitorare le performance di produzione.

            Query SQL:


            SELECT po.no AS order_no, prl.type AS operation_type, AVG(prl.quantity) AS quantita_media
            FROM production_orders po
            JOIN prodorderroutinglines prl ON po.no = prl.prodorder_no
            GROUP BY po.no, prl.type;




    Analisi dei costi operativi totali e medi per tipo di ordine e tipo di operazione:

            Domanda: Qual è il costo operativo totale e medio per ciascun tipo di ordine e tipo di operazione?

            Utilità per il Cliente: Fornisce una valutazione dettagliata dei costi operativi, consentendo al cliente di comprendere il costo complessivo e medio associato a tipi specifici di attività di produzione.

            Query SQL:


            SELECT prl.type, po.no AS order_no, SUM(cl.direct_cost + cl.overhead_cost) AS costo_totale, AVG(cl.direct_cost + cl.overhead_cost) AS costo_medio
            FROM prodorderroutinglines prl
            JOIN production_orders po ON prl.prodorder_no = po.no
            JOIN capacity_ledger cl ON prl.routing_no = cl.routing_no
            GROUP BY prl.type, po.no
            ORDER BY costo_totale DESC;




    Analisi del tempo di esecuzione per tipo di operazione e centro di lavoro:

            Domanda: Qual è il tempo di esecuzione medio per ciascun tipo di operazione e centro di lavoro?

            Utilità per il Cliente: Fornisce una visione dettagliata delle prestazioni relative al tempo di esecuzione delle operazioni, consentendo al cliente di identificare inefficienze e ottimizzare la distribuzione delle operazioni.

            Query SQL:


            SELECT prl.type, mc.name AS center_name, AVG(prl.run_time) AS tempo_medio_esecuzione
            FROM prodorderroutinglines prl
            JOIN machine_centers mc ON prl.work_center_no = mc.no
            GROUP BY prl.type, mc.name
            ORDER BY tempo_medio_esecuzione DESC;




    Analisi della quantità media prodotta per tipo di ordine, tipo di operazione e risorsa:

            Domanda: Qual è la quantità media prodotta per tipo di ordine, tipo di operazione e risorsa?

            Utilità per il Cliente: Offre una visione dettagliata della produzione in base a diversi criteri, consentendo al cliente di identificare le combinazioni più efficaci di tipo di ordine, tipo di operazione e risorsa.

            Query SQL:


            SELECT po.no AS order_no, prl.type AS operation_type, cl.routing_no, AVG(prl.quantity) AS quantita_media
            FROM production_orders po
            JOIN prodorderroutinglines prl ON po.no = prl.prodorder_no
            JOIN capacity_ledger cl ON prl.routing_no = cl.routing_no
            GROUP BY po.no, prl.type, cl.routing_no;




    Analisi del rapporto tra quantità prodotta e costi operativi:

            Domanda: Qual è il rapporto tra la quantità prodotta e i costi operativi per ciascun tipo di ordine e tipo di operazione?

            Utilità per il Cliente: Fornisce una valutazione della relazione tra la produzione e i costi operativi, aiutando il cliente a ottimizzare la redditività delle attività di produzione.

            Query SQL:


            SELECT po.no AS order_no, prl.type AS operation_type, SUM(cl.direct_cost + cl.overhead_cost) AS costo_totale, AVG(prl.quantity) AS quantita_media
            FROM production_orders po
            JOIN prodorderroutinglines prl ON po.no = prl.prodorder_no
            JOIN capacity_ledger cl ON prl.routing_no = cl.routing_no
            GROUP BY po.no, prl.type
            ORDER BY quantita_media DESC;




            