# Python version 3.11.0
# requests-ntlm 1.1.0
# mysql-connector-python 8.2.0
# schedule 1.2.1

import schedule
import time
from auth.auth import main as main_auth

# Flag per indicare se i lavori devono essere interrotti
stop_jobs = False

# Metodo che schedulo e fa partire l'applicazione
def run_jobs():
    main_auth()

# Metodo per stoppare la schedule
def stop_schedule():
    global stop_jobs
    stop_jobs = True
    # Cancella le esecuzioni di run_jobs
    schedule.clear()
    exit()

# Metodo main con la schedule
def main():
    # Esecuzione dello script ogni giorno alle ore 01:00
    schedule.every().day.at("01:00").do(run_jobs)

    try:
    # Loop per eseguire il programma
        while True:
            if stop_jobs:
                break

            schedule.run_pending()
            time.sleep(1)

    # Inserimento di un comando da tastiera (CTRL + C) per interrompere l'applicazione
    except KeyboardInterrupt:
        print("Programma interrotto dall'utente.")
        stop_schedule()

if __name__ == "__main__":
    main()
