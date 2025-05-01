
import threading
import queue
import time
import random
from Recursos import AsignadorRecursos


class Paciente(threading.Thread):
    def __init__(self, id_paciente, cola_registro, cola_diagnostico, cola_criticos, cola_estables, asignador_recursos):
        super().__init__()
        self.id_paciente = id_paciente
        self.cola_registro = cola_registro
        self.cola_diagnostico = cola_diagnostico
        self.cola_criticos = cola_criticos
        self.cola_estables = cola_estables
        self.asignador_recursos = asignador_recursos
        self.estado = None  # "critico" o "estable"

    def run(self):
        self.registro()
        self.espera_turno()
        self.diagnostico_inicial()
        self.espera_recursos()
        self.seguimiento_alta()

    def registro(self):
        print(f"Paciente {self.id_paciente} registrándose...")
        self.cola_registro.put(self.id_paciente)
        time.sleep(random.uniform(0.2, 0.5))

    def espera_turno(self):
        print(f"Paciente {self.id_paciente} esperando turno...")
        time.sleep(random.uniform(0.1, 0.4))

    def diagnostico_inicial(self):
        print(f"Paciente {self.id_paciente} recibiendo diagnóstico inicial...")
        self.estado = random.choices(["critico", "estable"], weights=[0.3, 0.7])[0]
        print(f"Paciente {self.id_paciente} diagnosticado como {self.estado.upper()}.")
        if self.estado == "critico":
            self.cola_criticos.put(self.id_paciente)
        else:
            self.cola_estables.put(self.id_paciente)

    def espera_recursos(self):
        if self.estado == "critico":
            print(f"Paciente {self.id_paciente} (CRÍTICO) esperando recursos prioritarios...")
            self.asignador_recursos.asignar(self.id_paciente, prioridad=True)
        else:
            # Esperar hasta que todos los críticos hayan sido atendidos
            while not self.cola_criticos.empty():
                print(f"Paciente {self.id_paciente} (ESTABLE) esperando porque hay críticos pendientes...")
                time.sleep(0.5)
            print(f"Paciente {self.id_paciente} (ESTABLE) esperando recursos...")
            self.asignador_recursos.asignar(self.id_paciente, prioridad=False)

    def seguimiento_alta(self):
        print(f"Paciente {self.id_paciente} en seguimiento y proceso de alta.")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Paciente {self.id_paciente} ha sido dado de alta.")

