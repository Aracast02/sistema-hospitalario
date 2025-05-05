import threading
import time
import random
 
class AsignadorRecursos:
    def __init__(self, doctores, camas):
        self.doctor_sem = threading.Semaphore(doctores)
        self.cama_sem = threading.Semaphore(camas)

    def asignar(self, id_paciente, prioridad=False):
        print(f"Paciente {id_paciente} esperando recursos...")
        with self.doctor_sem, self.cama_sem:
            print(f"Paciente {id_paciente} recibió doctor y cama.")
            tiempo_atencion = random.uniform(1, 2) if prioridad else random.uniform(2, 3)
            time.sleep(tiempo_atencion)
            print(f"Paciente {id_paciente} liberó recursos.")