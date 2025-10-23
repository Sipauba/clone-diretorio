import schedule
import time
import threading
from function_check_difference import function_check_difference
from function_copy import function_copy
from frame_entry_clone import entry_clone
from frame_entry_original import entry_original

def function_schedule(intervalo_horas=1):
    """
    Agenda a execução automática da cópia a cada X horas.
    Mantém o Tkinter livre (roda em thread separada).
    """

    from frame_entry_clone import entry_clone
    from frame_entry_original import entry_original

    path_original = entry_original.get()
    path_clone = entry_clone.get()

    schedule.clear()
    schedule.every(intervalo_horas).minutes.do(
        lambda:function_copy(path_original,path_clone))

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = threading.Thread(target=run_schedule, daemon=True)
    thread.start()
