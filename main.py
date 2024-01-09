# schdeule 1.2.1

import schedule
import time
from auth.auth import main as main_auth

def run_jobs():
    main_auth()

def stop_schedule():
    # Cancels all scheduled jobs and exits the program
    schedule.clear()
    exit()

def main():
    # Esecuzione dello script ogni giorno alle ore 01:00
    schedule.every().day.at("01:00").do(run_jobs)

    # Pianifica l'interruzione dello schedule dopo 60 secondi
    schedule.every(60).seconds.do(stop_schedule)

    # Loop per eseguire il programma
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
