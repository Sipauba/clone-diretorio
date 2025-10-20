import schedule
import time
import threading
from function_copy import function_copy
from tkinter import messagebox

def start_schedule(horario="23:00"):
    """
    Agenda a execução automática da cópia no horário especificado (HH:MM).
    Mantém o Tkinter livre (roda em thread separada).
    """
    schedule.clear()  # limpa agendamentos anteriores
    schedule.every().day.at(horario).do(function_copy)

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = threading.Thread(target=run_schedule, daemon=True)
    thread.start()
    messagebox.showinfo('Agendado', f"Cópia automática configurada para {horario} todos os dias.")