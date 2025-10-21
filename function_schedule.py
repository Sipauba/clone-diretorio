import schedule
import time
import threading
from function_check_difference import function_check_difference

def function_schedule(intervalo_horas=1):
    """
    Agenda a execução automática da cópia a cada X horas.
    Mantém o Tkinter livre (roda em thread separada).
    """
    schedule.clear()
    schedule.every(intervalo_horas).minutes.do(function_check_difference)

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = threading.Thread(target=run_schedule, daemon=True)
    thread.start()
